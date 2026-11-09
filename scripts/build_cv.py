#! /usr/bin/env python3
'''
Build CV
'''

# imports
from pathlib import Path
from sys import argv
import argparse

# constants
TEXT_EXTS = {'c', 'cpp', 'css', 'csv', 'h', 'hpp', 'htm', 'html', 'js', 'md', 'json', 'tsv', 'txt'}
TRANSLATE = {
    'Computer Science & Engineering (CSE)': 'Computer Science & Engineering',
    'Future Technology Group (FTG)': 'Future Technology Group',
    'University of California, San Diego (UCSD)': 'UC San Diego',
}

# translate a string
def translate(s):
    return TRANSLATE.get(s, s)

# parse user args
def parse_args():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--input', required=False, type=str, default=Path(argv[0]).expanduser().resolve().parent.parent, help="Root of GitHub Repository")
    parser.add_argument('-o', '--output', required=False, type=str, default='stdout', help="Output Markdown File")
    args = parser.parse_args()
    args.input = Path(args.input)
    for p in [args.input, args.input / 'data']:
        if not p.is_dir():
            raise ValueError(f"Directory not found: {p}")
    if args.output not in {'stdout', 'stderr'}:
        args.output = Path(args.output)
        if args.output.exists():
            raise ValueError(f"Output exists: {args.output}")
    return args

# load data: data[dir1][dir2][...] = string or None (denoting binary file)
def load_data(path):
    data = dict()
    for p in path.rglob('*'):
        if not p.is_file() or p.stem.strip().upper() == 'README':
            continue
        curr = data; parts = p.relative_to(path).parts
        for part_ind, part in enumerate(parts):
            if part_ind == (len(parts) - 1): # file
                ext = part.split('.')[-1].strip().lower()
                if ext in TEXT_EXTS:
                    with open(p, mode='rt') as f:
                        curr[part] = f.read().strip()
                else:
                    curr[part] = None # binary file
            else: # folder
                if part not in curr:
                    curr[part] = dict()
                curr = curr[part]
    return data

# build YAML front matter
def build_front_matter():
    out = '---\n'
    out += 'documentclass: scrartcl\n'
    out += 'fontsize: 10pt\n'
    out += 'papersize: letter\n'
    out += 'geometry: margin=0.75in\n'
    out += 'urlcolor: blue\n'
    out += 'mainfont: "TeX Gyre Pagella"\n'
    out += 'header-includes:\n'
    out += '  - |\n'
    out += '    \\setkomafont{disposition}{\\normalcolor\\rmfamily\\bfseries}\n'
    out += '    \\usepackage{enumitem}\\setlist[itemize]{itemsep=0.25em, topsep=0.25em}\\providecommand{\\tightlist}{}\\renewcommand{\\tightlist}{}\n'
    out += '---\n'
    return out

# build personal information section
def build_personal_info(site_data):
    out = '```{=latex}\n'
    out += '\\begin{center}\n'
    out += '{\\LARGE\\bfseries ' + site_data['first_name.txt'] + ' ' + site_data['last_name.txt'] + '}\\\\[6pt]\n'
    out += '\\href{mailto:' + site_data['email.txt'] + '}{' + site_data['email.txt'] + '}\n'
    out += '\\quad | \\quad\n'
    out += '\\href{' + site_data['url.txt'] + '}{' + site_data['url.txt'] + '}\n'
    out += '\\end{center}\n'
    out += '```\n'
    return out

# helper for sorting entries with start and end dates
def sort_helper_dates(x):
    if 'start_date.txt' in x:
        start_year, start_month, start_day = [int(s) for s in x['start_date.txt'].split('-')]
    else:
        start_year, start_month, start_day = [0]*3
    if 'end_date.txt' in x:
        end_year, end_month, end_day = [int(s) for s in x['end_date.txt'].split('-')]
    else:
        end_year, end_month, end_day = [9999, 99, 99]
    return (end_year, end_month, end_day, start_year, start_month, start_day)

# build education section
def build_education(edu_data):
    out = '# Education\n\n'
    for entry in sorted(edu_data.values(), key=sort_helper_dates, reverse=True):
        out += f"* **{entry['degree.txt']}**, {entry['major.txt']}, *{translate(entry['institution.txt'])}* ({entry['start_date.txt'].split('-')[0]}–{entry['end_date.txt'].split('-')[0]})\n\n"
    return out

# build (non-)academic positions
def build_positions(positions_data, header_text):
    out = f'# {header_text}\n\n'
    for entry in sorted(positions_data.values(), key=sort_helper_dates, reverse=True):
        if 'end_date.txt' in entry:
            end_year = entry['end_date.txt'].split('-')[0]
        else:
            end_year = 'Present'
        out += f"* **{entry['title.txt']}**, {translate(entry['department.txt'])}, *{translate(entry['institution.txt'])}* ({entry['start_date.txt'].split('-')[0]}–{end_year})\n\n"
    return out

# build CV markdown
def build_cv_markdown(repo_path):
    site_data = load_data(repo_path / 'site')
    data = load_data(repo_path / 'data')
    out = f'{build_front_matter()}\n'
    out += f'{build_personal_info(site_data)}\n'
    out += f"{build_education(data['positions']['education'])}\n"
    out += f"{build_positions(data['positions']['academic'], 'Academic Positions')}\n"
    out += f"{build_positions(data['positions']['non_academic'], 'Non-Academic Positions')}\n"
    pass # TODO
    return out

# main logic
def main():
    args = parse_args()
    md_text = build_cv_markdown(args.input)
    if isinstance(args.output, str):
        if args.output == 'stdout':
            from sys import stdout as out_f
        elif args.output == 'stderr':
            from sys import stderr as out_f
        else:
            raise ValueError(f"Invalid output: {args.output}")
    else:
        out_f = open(args.output, mode='wt')
    out_f.write(md_text)
    if not md_text.endswith('\n'):
        out_f.write('\n')
    out_f.close()

# run script
if __name__ == '__main__':
    main()
