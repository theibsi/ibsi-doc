# -*- coding: utf-8 -*-
import os
import re
import shutil
import tempfile

import six
from six.moves import range


def main():
  tex_source_folder = '../ibsi-reference-manual'
  tmp = tempfile.mkdtemp()
  try:
    shutil.copytree(tex_source_folder, os.path.join(tmp, 'ibsi-reference-manual'))

    tex_source = os.path.join(tmp, 'ibsi-reference-manual', 'IBSIWorkDocument.tex')
    feature_source = os.path.join(tex_source, '..', 'Chapters', 'FeatureDef.tex')

    tex_data = read_tex_source(tex_source)
    feature_data = read_tex_source(feature_source)

    feature_class_codes, feature_codes = parse_feature_ids(feature_data)
    other_codes = parse_other_ids(tex_data)

    tex_data, inline_codes = update_inline_ids(tex_data)
    with open(tex_source, mode='w') as tex_fs:
      tex_fs.write(tex_data)
    feature_data, feature_inline_codes = update_inline_ids(feature_data)
    with open(feature_source, mode='w') as feature_fs:
      feature_fs.write(feature_data)

    fix_benchmark_tables(os.path.join(tmp, 'ibsi-reference-manual', 'benchmarks'))

    figures = parse_tex_figures(tex_data)
    chap_labels = get_chapter_labels(tex_data)

    output = parse_input(tex_source)
    if output is None or output == '':
      raise ValueError('Empty output was returned!')
    output = output.replace('\r', '')

    output, footnotes = get_footnotes(output)

    output = correct_tables(output)
    output = parse_chapter_refs(output, chap_labels)

    output_lines = output.split('\n')
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

    footnote_ref_pattern = re.compile('\[(?P<no>\d+)\]_')

    for section, code_dict in split_sections(output_lines, feature_class_codes, feature_codes, other_codes, hdr_chars):

      for line in sorted(code_dict.keys(), reverse=True):
        section.insert(line + 2, '.. raw:: html\n\n  <p style="color:grey;font-style:italic;text-align:right">%s</p>' % code_dict[line][0])

      process_citations(section)
      fix_math_indent(section)
      fix_math_formula(section)
      fix_figures(section, figures)
      fix_numbered_lists(section)

      print('Storing section %s' % section[0])

      dest_name = section[0].replace(' ', '_')
      if cnt > 0:
        dest_name = '%-.2i_' % cnt + dest_name

      cnt += 1

      if cnt == 1:
        index.insert(0, '.. include:: %s.rst' % str(dest_name))
      else:
        index.append('   %s <%s>' % (section[0], dest_name))

      # Check if this chapter has a label in the source. If so, also add a label in the rst document
      section_title = section[0].lower()
      if section_title in chap_labels:
        section.insert(0, '.. _%s:\n' % chap_labels[section_title])

      out_str = u'\n'.join(section).encode('utf-8')

      section_footnotes = sorted([int(m.groupdict()['no']) for m in footnote_ref_pattern.finditer(out_str)])
      footer = ''
      for sf in section_footnotes:
        footer += u'\n.. [%i]\n   %s\n' % (sf, footnotes[sf])

      with open(dest_name + '.rst', mode='wb') as out_fs:
        out_fs.write(out_str)
        out_fs.write(footer)

    index.append('   References')
    index.append('')

    with open('index.rst', mode='w') as index_fs:
      out_str = u'\n'.join(index).encode('utf-8')
      index_fs.write(out_str)

    print (hdr_chars)
  finally:
    shutil.rmtree(tmp)


def parse_input(source_file):
  import pypandoc

  print('PyPandoc version: %s' % pypandoc.__version__)

  current_dir = os.path.abspath(os.path.curdir)
  source_dir = os.path.dirname(source_file)

  if not os.path.isdir(source_dir):
    raise ValueError('Directory "%s" does not exist, cannot convert')

  if not (source_dir == '' or source_dir == '.'):
    os.chdir(source_dir)

  try:
    return pypandoc.convert_file(source_file, to='rst', extra_args=['--mathjax'])
  finally:
    os.chdir(current_dir)


def split_sections(output_lines, feature_class_codes, feature_codes, other_codes, header_chars=None):
  if header_chars is None:
    header_chars = []
  current_level = -1
  start_line = -1
  corrected_header_chars = {}

  class_idx = 0
  feature_idx = 0
  code_idx = 0

  code_dict = {}

  for line_idx in range(len(output_lines)):
    line = output_lines[line_idx]
    if len(line) < 2:
      continue
    if line == line[0] * len(line) and len(line) == len(output_lines[line_idx - 1]):
      # Section header!
      title = output_lines[line_idx - 1].replace(u'’', "'")

      if class_idx < len(feature_class_codes) and title == feature_class_codes[class_idx][1]:
        code_dict[line_idx - 1 - start_line] = feature_class_codes[class_idx]
        class_idx += 1
      elif feature_idx < len(feature_codes) and title == feature_codes[feature_idx][1]:
        code_dict[line_idx - 1 - start_line] = feature_codes[feature_idx]
        feature_idx += 1
      elif code_idx < len(other_codes) and title == other_codes[code_idx][1]:
        code_dict[line_idx - 1 - start_line] = other_codes[code_idx]
        code_idx += 1

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
          yield output_lines[start_line: line_idx - 1], code_dict  # Line above header line is Title, don't include that in the previous section
        start_line = line_idx - 1
        code_dict = {}

  yield output_lines[start_line:], code_dict  # return the remainder of the document


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


def read_tex_source(tex_source):
  """
  Read the source Tex document. Raises a ValueError if the file is not found.

  :param tex_source: Tex base file of the IBSI document
  :return: string of the file contents
  """
  if not os.path.isfile(tex_source):
    raise ValueError('Tex source file (%s) is not found!' % tex_source)

  with open(tex_source, mode='r') as tex_fs:
    return tex_fs.read()


def parse_tex_figures(tex_data):
  """
  Figures in Tex are not parsed correctly by pandoc.

  For example, \label and \scale are ignored, and caption is copied to alt:

  :param tex_data: Source document contents (result of py:func:`read_tex_source`)
  :return: a dictionary containing the Tex defined filename as key, and the replacement lines as value (list)
  """
  figures = {}

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


def parse_feature_ids(features_tex):
  feat_pattern = re.compile(
    r'\\(sub)?section\[.+\]\{(?P<FeatureName>.+)\\id\{(?P<FeatureCode>\w{4})\}\}( ?\\label\{(?P<FeatureLabel>.+)\})?'
  )
  feature_codes = []
  class_codes = []
  for match in feat_pattern.finditer(features_tex):
    g = match.group(0)
    is_class = match.group(1) is None
    d = match.groupdict()

    feature_name = d['FeatureName']

    feature_name = feature_name.replace('\\textsuperscript{th}', '\\ :sup:`th`')

    if is_class:
      class_codes.append((d['FeatureCode'], feature_name, d['FeatureLabel']))
    else:
      feature_codes.append((d['FeatureCode'], feature_name, d['FeatureLabel']))

  return class_codes, feature_codes


def parse_other_ids(source_tex):
  feat_pattern = re.compile(
    r'\\(sub)*section((\[.+\])|\*)\{(?P<FeatureName>.+)\\id\{(?P<FeatureCode>\w{4})\}\}( ?\\label\{(?P<FeatureLabel>.+)\})?'
  )
  other_codes = []
  for match in feat_pattern.finditer(source_tex):
    g = match.group(0)
    d = match.groupdict()

    feature_name = d['FeatureName']

    feature_name = feature_name.replace('\\textsuperscript{th}', '\\ :sup:`th`')

    other_codes.append((d['FeatureCode'], feature_name, d['FeatureLabel']))

  return other_codes


def update_inline_ids(source_tex):
  id_pattern = re.compile(r'\\textid{(?P<InlineCode>\w{4})}')

  inline_codes = set()
  for match in id_pattern.finditer(source_tex):
    inline_codes.add(match.groupdict()['InlineCode'])

  source_tex, n = id_pattern.subn(r'\\textit{\g<InlineCode>}', source_tex)
  print('replaced %i instances of an inline ID (%s)' % (n, inline_codes))
  return source_tex, inline_codes


def fix_benchmark_tables(benchmark_dir):
  small_pattern = re.compile(r'\\small{(?P<table>(.*\n)+)}\n')
  table_pattern = re.compile(r'\\begin{longtable}{ccccc}\n\s+\\toprule\n(?P<hdr>({\\textbf{.+}} & )+{\\textbf{.+}}\s)\\\\\s*\n\s+\\midrule\n(?P<table_data>(.+\\\\\s*\n)+\s+\\bottomrule)(?P<caption>\n\\caption{)')
  em_dash_pattern = re.compile(r'\\textemdash')

  def header_fix(match):
    grps = match.groupdict()
    header = grps['hdr']
    repl = '\\begin{longtable}\n\\centering\n\\begin{tabular}{ccccc}\n  \\toprule\n'
    repl += re.sub(r'{(?P<hdr>\\textbf{[a-z\. ]+})} ', '\g<hdr> ', header)
    repl += '\\\\ \n  \\midrule\n'
    repl += grps['table_data']
    repl += '\n\\end{tabular}'
    repl += grps['caption']
    return repl

  for fname in os.listdir(benchmark_dir):
    with open(os.path.join(benchmark_dir, fname)) as b_fs:
      b_table = b_fs.read()
    b_table = small_pattern.sub(r'\\small\g<table>', b_table)
    b_table = table_pattern.sub(header_fix, b_table)
    b_table = em_dash_pattern.sub('---', b_table)
    with open(os.path.join(benchmark_dir, fname), mode='w') as b_fs:
      b_fs.write(b_table)


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

    for k in ('align',):  # ('scale', 'align'):
      if k in fig_data:
        fig.append(u'   :%s: %s' % (k, fig_data[k].strip()))

    section_lines[r[0]:r[1]] = fig


def fix_numbered_lists(section_lines):
  is_list = False
  for line_idx in range(len(section_lines)):
    line = section_lines[line_idx]
    if line.startswith('#. '):
      is_list = True
    elif is_list:
      if line == '':
        is_list = False
      else:
        m = re.match(r'(?P<indent>\s*)\S', line)
        indent = m.groupdict()['indent']
        if indent != '   ':
          section_lines[line_idx] = '   ' + line[len(indent):]


def correct_tables(total_output):
  pattern = r'(^\n|(\| \n)|(\|? ?to 0\.\d+\n)|(@\S+@\n))*(?P<table_data>(^\| [^\&\n]*( ?\&[^\&\n]*)+\n(  (\S+\s)+)*\n*)+)'

  replacements = {}

  for match in re.finditer(pattern, total_output, flags=re.MULTILINE):
    table = match.groupdict()['table_data']
    rows = table.split('|')[1:]
    rows = [r.replace('\n', '').split('&') for r in rows]

    rows = [r for r in rows if len(r) == len(rows[-1])]

    new_table = '\n.. list-table::\n   :widths: auto\n'

    headers = True
    hdrlines = 0
    for r in rows:
      if headers:
        if all([c.strip().startswith('**') and c.strip().endswith('**') for c in r]):
          hdrlines += 1
        else:
          headers = False

    if hdrlines > 0:
      new_table += '   :header-rows: %i\n' % hdrlines
    for r_idx, r in enumerate(rows):
      if r_idx < hdrlines:
        r = [c.strip()[2:-2] for c in r]
      new_table += '\n   * - %s' % '\n     - '.join(r)

    new_table += '\n\n'

    replacements[(match.start(), match.end())] = new_table

  for r in sorted(replacements, key=lambda x: x[0], reverse=True):
    total_output = total_output[:r[0]] + replacements[r] + total_output[r[1]:]

  return total_output


def get_chapter_labels(tex_data):
  """

  :param tex_data: Source document contents (result of py:func:`read_tex_source`)
  :return:
  """
  chap_labels = {}

  for match in re.finditer(r'\\chapter.?\{(?P<Chapter>(\w+)( \w+)*)\}\\label\{(?P<Label>(\w+)([ _]\w+)*)\}', tex_data):
    chap_labels[match.groupdict()['Chapter'].lower()] = match.groupdict()['Label'].replace(' ', '_')
  return chap_labels


def parse_chapter_refs(output, chapter_labels):
  refs = chapter_labels.viewvalues()

  replacements = {}
  for match in re.finditer(r'\(\*\*Chapter[ \n]\[(?P<chapter>chap(\\_\w+)+( \w+)?)\]\*\*\)', output):
    chapter_ref = match.groupdict()['chapter'].replace(r'\_', '_').replace(' ', '_')
    if chapter_ref not in refs:
      print("Skipping ref %s (could not find corresponding chapter)" % chapter_ref)
      chapter_ref = None
    match_str = match.group()
    replacements[match_str] = chapter_ref

  for r in replacements:
    if replacements[r] is None:
      r_str = ''
    else:
      r_str = '(:ref:`%s`)' % replacements[r]
    if '\n' in r:
      r_str = '\n' + r_str
    output = output.replace(r, r_str)
  return output


def get_footnotes(output):
  footnotes = {}
  footnote_pattern = re.compile(r'\n.. \[(?P<no>\d+)\]\s*\n\s+(?P<value>.+)\n')
  for m in footnote_pattern.finditer(output):
    grp = m.groupdict()
    footnotes[int(grp['no'])] = grp['value']

  output = footnote_pattern.sub('', output)
  return output, footnotes


if __name__ == '__main__':
  os.chdir(r'..\docs')
  main()
