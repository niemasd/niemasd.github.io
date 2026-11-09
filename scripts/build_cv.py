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
    'Centers for Disease Control and Prevention (CDC)': 'CDC',
    'Collaborative Program Grant for Multidisciplinary Teams (RM1)': 'RM1',
    'Education Projects (R25)': 'R25',
    'Google Cloud Platform (GCP) Research Credits Program': 'GCP Research Credits Program',
    'institutional': 'Institutional Service',
    'National Institutes of Health (NIH)': 'NIH',
    'National Science Foundation (NSF)': 'NSF',
    'online': 'Online',
    'Specialized Center - Cooperative Agreements (U54)': 'U54',
    'ucsd': 'UC San Diego',
    'University of California - Hispanic-Serving Institution (UC-HSI) Doctoral Diversity Initiative (DDI)': 'UC-HSI DDI',
    'University of California Office of the President (UCOP)': 'UCOP',
    'University of California, San Diego (UCSD)': 'UC San Diego',
}

# translate a string
def translate(s):
    return TRANSLATE.get(s, s.split(' (')[0])

# parse author list
def parse_authors(authors_text, owner_name=None):
    authors = list()
    for author_row in [l.strip() for l in authors_text.splitlines() if len(l.strip()) != 0]:
        first_name, last_name = [s.strip() for s in author_row.split(',')]
        abbrev_name = f"{last_name} {''.join(s[0] for s in first_name.replace('-',' ').split()).upper()}".strip()
        if f'{first_name} {last_name}' == owner_name:
            authors.append(f'**{abbrev_name}**')
        else:
            authors.append(abbrev_name)
    return ', '.join(authors)

# helper for sorting entries with start and end dates
def sort_helper_dates(x, end_first=True):
    if 'start_date.txt' in x:
        start_year, start_month, start_day = [int(s) for s in x['start_date.txt'].split('-')]
    else:
        start_year, start_month, start_day = [0]*3
    if 'end_date.txt' in x:
        end_year, end_month, end_day = [int(s) for s in x['end_date.txt'].split('-')]
    else:
        end_year, end_month, end_day = [9999, 99, 99]
    if end_first:
        return (end_year, end_month, end_day, start_year, start_month, start_day)
    else:
        return (start_year, start_month, start_day, end_year, end_month, end_day)
def sort_helper_start_dates(x):
    return sort_helper_dates(x, end_first=False)
def sort_helper_end_dates(x):
    return sort_helper_dates(x, end_first=True)

# helper for sorting courses
def sort_helper_courses(x):
    if 'course_num.txt' in x:
        if ' ' in x['course_num.txt']:
            dept, num = [s.strip().upper() for s in x['course_num.txt'].split(' ')]
            num_digits = ''
            for c in num:
                if '0' <= c <= '9':
                    num_digits += c
                else:
                    break
            num_digits = int(num_digits)
            num_letters = ''
            for c in num[::-1]:
                if '0' <= c <= '9':
                    break
                else:
                    num_letters += c
            num_letters = num_letters[::-1].strip()
        else:
            dept = x['course_num.txt']; num_digits = 0; num_letters = ''
        return (dept, num_digits, num_letters, x['title.txt'])
    else:
        return ('', 0, '', x['title.txt'])

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
    out += '\\noindent\n'
    out += '{\\LARGE\\bfseries ' + site_data['first_name.txt'] + ' ' + site_data['last_name.txt'] + '}\n'
    out += '\\hfill\n'
    out += '\\href{mailto:' + site_data['email.txt'] + '}{' + site_data['email.txt'] + '}\n'
    out += '\\quad | \\quad\n'
    out += '\\href{' + site_data['url.txt'] + '}{' + site_data['url.txt'] + '}\n'
    out += '```\n'
    return out

# build education section
def build_education(edu_data):
    out = '# Education\n\n'
    for entry in sorted(edu_data.values(), key=sort_helper_end_dates, reverse=True):
        out += f"* **{entry['degree.txt']}**, {entry['major.txt']}, *{translate(entry['institution.txt'])}* ({entry['start_date.txt'].split('-')[0]}–{entry['end_date.txt'].split('-')[0]})\n"
    return out

# build (non-)academic positions
def build_positions(positions_data, header_text):
    out = f'# {header_text}\n\n'
    for entry in sorted(positions_data.values(), key=sort_helper_end_dates, reverse=True):
        if 'end_date.txt' in entry:
            end_year = entry['end_date.txt'].split('-')[0]
        else:
            end_year = 'Present'
        out += f"* **{entry['title.txt']}**"
        if 'department.txt' in entry:
            out += f", {translate(entry['department.txt'])}"
        if 'institution.txt' in entry:
            out += f", *{translate(entry['institution.txt'])}*"
        out += f" ({entry['start_date.txt'].split('-')[0]}–{end_year})\n"
    return out

# build funding section
def build_funding(funding_data):
    out = '# Funding\n\n'
    for entry in sorted(funding_data.values(), key=sort_helper_start_dates, reverse=True):
        out += f"* {translate(entry['awarder.txt'])}"
        if 'program.txt' in entry:
            out += f" {translate(entry['program.txt'])}"
        if 'award_num.txt' in entry:
            out += f" {entry['award_num.txt']}"
        out += f" (**{entry['amount.txt']}**; {entry['start_date.txt'].split('-')[0]}–{entry['end_date.txt'].split('-')[0]})\n"
        out += f"  * *{entry['title.txt']}*\n"
    return out

# build honors section
def build_honors(honors_data):
    out = '# Honors and Awards\n\n'
    for entry in sorted(honors_data.values(), key=sort_helper_start_dates, reverse=True):
        out += f"* **{entry['title.txt']}**"
        if 'program.txt' in entry:
            out += f", {translate(entry['program.txt'])}"
        out += f", *{translate(entry['awarder.txt'])}* ({entry['start_date.txt'].split('-')[0]})\n"
    return out

# build research section
def build_research(research_data, owner_name=None):
    out = f'# Research\n\n'
    for k in ['papers', 'talks', 'conferences', 'preprints', 'books', 'games']:
        out += f'## {k.title()}\n\n'
        for entry in sorted(research_data[k].values(), key=lambda x: x['date.txt'], reverse=True):
            out += f'''* {parse_authors(entry['authors.csv'], owner_name=owner_name)} ({entry['date.txt'].split('-')[0]}). "{entry['title.txt']}." *{entry['venue.txt']}*'''
            if 'location.txt' in entry:
                out += f", {entry['location.txt']}"
            out += '. '
            if 'volume.txt' in entry:
                out += entry['volume.txt']
            if 'issue.txt' in entry:
                out += f"({entry['issue.txt']})"
            if 'pages.txt' in entry:
                if 'volume.txt' in entry or 'issue.txt' in entry:
                    out += ':'
                out += entry['pages.txt'].replace('-','–')
            if 'volume.txt' in entry or 'issue.txt' in entry or 'pages.txt' in entry:
                out += '.'
            if 'type.txt' in entry:
                out += f" {entry['type.txt']}."
            for ID_type, ID_fn, ID_url_base in [
                ('doi', 'doi.txt', 'https://doi.org/'),
                ('arXiv', 'arxiv.txt', 'https://arxiv.org/abs/'),
                ('ISBN', 'isbn.txt', 'http://books.google.com/books?vid=ISBN'),
                ('ASIN', 'asin.txt', 'https://www.amazon.com/dp/'),
                ('MobyGames', 'mobygames.txt', 'https://www.mobygames.com/game/'),
                ('Steam', 'steam.txt', 'https://store.steampowered.com/app/'),
            ]:
                if ID_fn in entry:
                    out += f" [{ID_type}:{entry[ID_fn]}]({ID_url_base}{entry[ID_fn]})."
            if 'url.txt' in entry:
                out += f" [Link]({entry['url.txt']})."
            out += '\n'
        out += '\n'
    return out

# build teaching section
def build_teaching(teaching_data):
    out = f'# Teaching\n\n'
    for k in ['ucsd', 'online']:
        out += f'## {translate(k)}\n\n'
        for entry in sorted(teaching_data[k].values(), key=sort_helper_courses):
            title = entry['title.txt']
            if 'course_num.txt' in entry:
                title = f"{entry['course_num.txt']}: {title}"
            if 'url.txt' in entry:
                title = f"[{title}]({entry['url.txt']})"
            out += f"* {title}\n"
        out += '\n'
    return out

def build_editor_reviewer(editor_reviewer_data, header):
    out = f'# {header}\n\n'
    for entry in sorted(editor_reviewer_data.values(), key=lambda x: x['institution.txt'].lower()):
        out += f"* [{entry['institution.txt']}]({entry['url.txt']})"
        if 'title.txt' in entry:
            out += f" ({entry['title.txt']})"
        out += '\n'
    return out

# build CV markdown
def build_cv_markdown(repo_path):
    # load data and set things up
    site_data = load_data(repo_path / 'site')
    data = load_data(repo_path / 'data')
    owner_name = site_data['first_name.txt'] + ' ' + site_data['last_name.txt']

    # build CV markdown
    out = f'{build_front_matter()}\n'
    out += f'{build_personal_info(site_data)}\n'
    out += f"{build_education(data['positions']['education'])}\n"
    out += f"{build_positions(data['positions']['academic'], 'Academic Positions')}\n"
    out += f"{build_positions(data['positions']['non_academic'], 'Non-Academic Positions')}\n"
    out += f"{build_funding(data['awards']['funding'])}\n"
    out += f"{build_honors(data['awards']['honors'])}\n"
    out += f"{build_research(data['research'], owner_name=owner_name)}\n"
    out += f"{build_teaching(data['teaching'])}\n"
    for k in ['editor', 'reviewer']:
        out += f"{build_editor_reviewer(data['positions'][k], k.title())}\n"
    for k in ['organizations', 'institutional', 'outreach']:
        out += f"{build_positions(data['positions'][k], translate(k).title())}\n"
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
