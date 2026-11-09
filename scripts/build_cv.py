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
    out += '\\vspace{0.5em}\n'
    out += '```\n'
    return out

# build education section
def build_education(edu_data):
    out = '# Education\n'
    out += 'TODO\n'
    return out

# build CV markdown
def build_cv_markdown(repo_path):
    site_data = load_data(repo_path / 'site')
    data = load_data(repo_path / 'data')
    out = f'{build_front_matter()}\n'
    out += f'{build_personal_info(site_data)}\n'
    out += f"{build_education(data['positions']['education'])}\n"
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
