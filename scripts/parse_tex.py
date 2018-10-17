import os
import re

import six
from six.moves import range


def main():
  tex_source = r'..\ibsi-reference-manual\IBSIWorkDocument.tex'
  output = parse_input(tex_source)
  figures = parse_tex_figures(tex_source)
  if output is None or output == '':
    raise ValueError('Empty output was returned!')

  output_lines = output.replace('\r', '').split('\n')
  hdr_chars = ['=', '-']
  index = [
    '',
    'Contents',
    '--------',
    '',
    '.. toctree::',
    '   :hidden:',
    '',
    '   Home <self>',
    '',
    '.. toctree::',
    '   :maxdepth: 2',
    ''
    ]

  cnt = 0
  for section in split_sections(output_lines, hdr_chars):
    cnt += 1
    process_citations(section)
    fix_math_indent(section)
    fix_math_formula(section)
    fix_figures(section, figures)

    out_str = u'\n'.join(section).encode('utf-8')
    print('Storing section %s' % section[0])

    dest_name = '%-.2i_' % cnt + section[0].replace(' ', '_')

    with open(dest_name + '.rst', mode='wb') as out_fs:
      out_fs.write(out_str)

    if cnt == 1:
      index.insert(0, '.. include:: %s.rst' % str(dest_name))
    else:
      index.append('   %s <%s>' % (section[0], dest_name))

  index.append('   References')
  index.append('')

  with open('index.rst', mode='w') as index_fs:
    out_str = u'\n'.join(index).encode('utf-8')
    index_fs.write(out_str)

  print (hdr_chars)


def parse_input(source_file):
  import pypandoc

  current_dir = os.path.abspath(os.path.curdir)
  source_dir = os.path.dirname(source_file)

  if not os.path.isdir(source_dir):
    raise ValueError('Directory "%s" does not exist, cannot convert')

  if not (source_dir == '' or source_dir == '.'):
    os.chdir(source_dir)

  try:
    return pypandoc.convert_file(os.path.basename(source_file), to='rst', extra_args=['--mathjax'])
  finally:
    os.chdir(current_dir)


def split_sections(output_lines, header_chars=None):
  if header_chars is None:
    header_chars = []
  current_level = -1
  start_line = -1
  corrected_header_chars = {}

  for line_idx in range(len(output_lines)):
    line = output_lines[line_idx]
    if len(line) < 2:
      continue
    if line == line[0] * len(line) and len(line) == len(output_lines[line_idx - 1]):
      # Section header!
      header_char = line[0]

      # Check if the header character is correct
      if header_char in corrected_header_chars:
        current_level = corrected_header_chars[header_char]
        output_lines[line_idx] = len(line) * header_chars[current_level]
      elif header_char not in header_chars:
        # header character not yet known, i.e. proceed to next level
        current_level += 1
        if (current_level + 1) > len(header_chars):
          # Level not yet reached,
          # store current header character as the character for the new level
          header_chars.append(header_char)
        else:
          # Next level was already known, but under a different character.
          # Update this header to the known character for this level
          output_lines[line_idx] = len(line) * header_chars[current_level]
          corrected_header_chars[header_char] = current_level
      elif header_chars.index(header_char) < current_level:
        # Character known, indicating a lower level. Go to that level
        current_level = header_chars.index(header_char)
        corrected_header_chars = {k: v for k, v in six.iteritems(corrected_header_chars) if v <= current_level}
      elif header_chars.index(header_char) > current_level:
        # Character known, indicating a higher level. Go to next level
        current_level += 1
        # Check if the character is correct
        if header_chars[current_level] != header_char:
          # Character not correct, update to the correct character
          output_lines[line_idx] = len(line) * header_chars[current_level]
          corrected_header_chars[header_char] = current_level

      # Check if the current level indicates a split section (main sections)
      if current_level == 0:
        # Yes it does! return the previous section and continue
        if start_line > -1:
          yield output_lines[start_line: line_idx - 1]  # Line above header line is Title, don't include that in the previous section
        start_line = line_idx - 1

  yield output_lines[start_line:]  # return the remainder of the document


def process_citations(section_lines):
  cite_pattern = r':raw-latex:`\\cite[pt]?\{(?P<Authors>[a-z,A-Z]+(-[a-z,A-Z]+)*\d{4}[a-z,A-Z]*(,\s?([a-z,A-Z]+(-[a-z,A-Z]+)*\d{4}[a-z,A-Z]*))*)\}`'

  for line_idx in range(len(section_lines)):
    line = section_lines[line_idx]
    replacements = {}
    for match in re.finditer(cite_pattern, line):
      match_str = match.group()
      authors = match.groupdict()['Authors'].split(',')

      replacements[match_str] = [a.strip() for a in authors]

    for r in replacements:
      r_str = ':cite:`' + ','.join(replacements[r]) + '`'
      if not (line.index(r) == 0 or line[line.index(r) - 1] == ' '):
        r_str = ' ' + r_str
      line = line.replace(r, r_str)
    section_lines[line_idx] = line


def fix_math_indent(section_lines):

  math_block = False
  math_line = False
  indent = None
  for line_idx in range(len(section_lines)):
    line = section_lines[line_idx]

    if line == '':
      continue

    if re.match('\s*.. math::$', line):
      math_block = True
    elif re.match('\s*.. math::', line):
      math_line = True
    elif math_block:
      if indent is None:
        indent = re.match('\s*', line).group()
      elif not re.match(indent + '\S', line):
        indent = None
        math_block = False
        section_lines[line_idx] = line.strip()
    elif math_line and line.startswith(' '):
      math_line = False
      section_lines[line_idx] = line.strip()


def fix_math_formula(section_lines):
  keys = {r'\floor*{': (r'\left\lfloor ', r'\right\rfloor '),
          r'\ceil*{': (r'\left\lceil ', r'\right\rceil '),
          r'\abs{': ('|', '|'),
          r'\norm{': (r'\|', r'\|'),
          r'\iverson{': (r'\big[', r'\big]')}
  regex = r'\\(floor\*|ceil\*|abs|norm|iverson)\{'

  for line_idx in range(len(section_lines)):
    line = section_lines[line_idx]

    replacements = []
    for match in re.finditer(regex, line):
      idx = match.start(), match.end()
      key = line[idx[0]:idx[1]]

      end_idx = None
      level = 1
      for char_idx, char in enumerate(line[idx[1]:], start=idx[1]):
        if char == '{':
          level += 1
        elif char == '}':
          level -= 1

        if level == 0:
          end_idx = char_idx
          break

      replacements.append((idx[0], idx[1], keys[key][0]))
      replacements.append((end_idx, end_idx + 1, keys[key][1]))

    if len(replacements) > 0:
      for r in sorted(replacements, key=lambda x: x[0], reverse=True):
        line = line[:r[0]] + r[2] + line[r[1]:]
      section_lines[line_idx] = line


def parse_tex_figures(tex_source):
  """
  Figures in Tex are not parsed correctly by pandoc.

  For example, \label and \scale are ignored, and caption is copied to alt:

  :param tex_source: Tex base file of the IBSI document
  :return: a dictionary containing the Tex defined filename as key, and the replacement lines as value (list)
  """

  if not os.path.isfile(tex_source):
    raise ValueError('Tex source file (%s) is not found!' % tex_source)

  figures = {}
  with open(tex_source, mode='r') as tex_fs:
    tex_data = tex_fs.read()

  for match in re.finditer(r'\\begin\{figure\}.*\n(?P<fig_data>(.+\n)+)\\end\{figure\}', tex_data):
    figure_data = match.groupdict()['fig_data']
    fig_elements = {}

    if r'\centering' in figure_data:
      fig_elements['align'] = 'center'
    caption = re.search(r'\\caption\{(.+)\}', figure_data)
    if caption:
      fig_elements['caption'] = caption.group(1)
    label = re.search(r'\\label\{(.+)\}', figure_data)
    if label:
      fig_elements['label'] = label.group(1)

    for graphics_sec in re.finditer(r'\\includegraphics(\[.*scale=(?P<scale>0\.\d+)\])?\{(?P<fig_name>.+)\}', figure_data):
      fig_name = graphics_sec.groupdict()['fig_name']

      figures[fig_name] = fig_elements.copy()

      scale = graphics_sec.groupdict().get('scale')
      if scale:
        figures[fig_name]['scale'] = str(int(float(scale) * 100))

  return figures


def fix_figures(section_lines, figures):
  fig_start = None
  indent = None

  replacements = []

  for line_idx in range(len(section_lines)):
    line = section_lines[line_idx]

    if line.startswith('.. figure:: '):
      fig_name = line.replace('.. figure:: ', '')
      fig_start = line_idx
    elif fig_start is not None:
      if indent is None:
        indent = re.match('\s*', line).group()
      elif line == '' or not re.match(indent + '\S', line):
        indent = None
        fig_end = line_idx

        #while section_lines[fig_end] == '':
        #  fig_end -= 1
        replacements.append((fig_start, fig_end, fig_name))

        fig_start = None

  for r in replacements[::-1]:
    fig = []
    fig_data = figures.get(r[2], {})
    if 'label' in fig_data:
      fig.append(u'.. _%s:' % fig_data['label'])

    fig.append(u'.. figure:: ' + r[2].replace('.pdf', '.png'))

    for k in ('scale', 'align'):
      if k in fig_data:
        fig.append(u'   :%s: %s' % (k, fig_data[k].strip()))

    section_lines[r[0]:r[1]] = fig


if __name__ == '__main__':
  os.chdir(r'..\docs')
  main()
