import os
import re

import bibtexparser
import six
from six.moves import range


def main():
  tex_source = r'..\ibsi-reference-manual\IBSIWorkDocument.tex'
  output = parse_input(tex_source)
  figures = parse_tex_figures(tex_source)
  if output is None or output == '':
    raise ValueError('Empty output was returned!')

  citation_data = parse_bibliography(r'..\ibsi-reference-manual\Bibliography.bib')
  #for entry in citation_data.entries:
  #  print (entry['ID'], u'\xe6' in entry['ID'])

  output_lines = output.replace('\r', '').split('\n')
  hdr_chars = ['=', '-']
  index = [
    'Welcome to the documentation of the IBSI',
    '========================================',
    '',
    '.. toctree::',
    '   :hidden:',
    '',
    '   Home < self >',
    '',
    '.. toctree::',
    '   :maxdepth: 2'
    ''
    ]

  for section in split_sections(output_lines, hdr_chars):
    process_citations(section, citation_data)
    fix_math_block(section)
    fix_figures(section, figures)

    out_str = u'\n'.join(section).encode('utf-8')
    print('Storing section %s' % section[0])
    with open(section[0].replace(' ', '_')+'.rst', mode='wb') as out_fs:
      out_fs.write(out_str)
    index.append('  %s <%s>' % (section[0], section[0].replace(' ', '_')))

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


def parse_bibliography(bib_file):
  with open(bib_file) as bib_fs:
    return bibtexparser.load(bib_fs)


def process_citations(section_lines, citation_data):
  cite_pattern = r':raw-latex:`\\cite[pt]?\{(?P<Authors>[a-z,A-Z]+(-[a-z,A-Z]+)*\d{4}[a-z,A-Z]*(,\s?([a-z,A-Z]+(-[a-z,A-Z]+)*\d{4}[a-z,A-Z]*))*)\}`'

  citations = {}

  for line_idx in range(len(section_lines)):
    line = section_lines[line_idx]
    replacements = {}
    for match in re.finditer(cite_pattern, line):
      match_str = match.group()
      authors = match.groupdict()['Authors'].split(',')

      replacements[match_str] = []
      for a in authors:
        a = a.strip()
        if a not in citations:
          a_data = citation_data.entries_dict.get(a)
          if a_data is None:
            continue
          citation, url = _format_citation(a_data)
          citations[a] = (len(citations) + 1, citation, url)

        replacements[match_str].append('%i_' % citations[a][0])

    for r in replacements:
      r_str = '\[' + ', '.join(replacements[r]) + '\]'
      if not (line.index(r) == 0 or line[line.index(r) - 1] == ' '):
        r_str = ' ' + r_str
      line = line.replace(r, r_str)
    section_lines[line_idx] = line

  for c, v in sorted(six.iteritems(citations), key=lambda x: x[1][0]):
    if v[2] is not None:
      link = '`%s <%s>`_' % (v[1], v[2])
    else:
      link = v[1]
    section_lines.append('.. [%i] %s' % (v[0], link))


def _format_citation(record):
  citation = []
  if not isinstance(record['author'], list):
    record = bibtexparser.customization.author(record)

  # Authors
  authors = record['author']
  if len(authors) > 6:
    citation.append(', '.join(authors[:6] + ['et al.']).replace('{', '').replace('}', ''))
  else:
    citation.append(', '.join(authors).replace('{', '').replace('}', ''))

  # Title
  citation.append('*%s*' % record['title'].replace('{', '').replace('}', ''))

  if 'journal' in record:
    citation.append(record['journal'].replace('{', '').replace('}', ''))
  if 'year' in record:
    citation.append(record['year'])
  if 'volume' in record:
    vol = record['volume']
    if 'number' in record:
      vol = vol + ' (%s)' % record['number']
    citation.append(vol)
  if 'pages' in record:
    citation.append(record['pages'])

  url = None
  if 'url' in record:
    url = record['url'].split(' ')[0].replace('{', '').replace('}', '')
  elif 'doi' in record:
    url = 'https://doi.org/' + record['doi'].replace('{', '').replace('}', '')

  return '; '.join(citation), url


def fix_math_block(section_lines):

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
    fig_name = None

    if r'\centering' in figure_data:
      fig_elements['align'] = 'center'
    if r'\includegraphics' in figure_data:

      graphics_sec = re.search(r'\\includegraphics(\[.*scale=(?P<scale>0\.\d+)\])?\{(?P<fig_name>.+)\}', figure_data)

      fig_name = graphics_sec.groupdict()['fig_name']
      scale = graphics_sec.groupdict().get('scale')
      if scale:
        fig_elements['scale'] = str(int(float(scale) * 100))

    caption = re.search(r'\\caption\{(.+)\}', figure_data)
    if caption:
      fig_elements['caption'] = caption.group(1)
    label = re.search(r'\\label\{(.+)\}', figure_data)
    if label:
      fig_elements['label'] = label.group(1)

    if fig_name:
      figures[fig_name] = fig_elements

  return figures


def fix_figures(section_lines, figures):
  fig_start = None
  indent = None

  replacements = []

  for line_idx in range(len(section_lines)):
    line = section_lines[line_idx]

    if line.startswith('.. figure:: '):
      fig_name = line.replace('.. figure:: ', '')
      if fig_name in figures:
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

  for r in replacements:
    fig = []
    fig_data = figures[r[2]]
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
