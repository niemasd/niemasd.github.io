#! /usr/bin/env python3
'''
Build personal website
'''

# imports
from datetime import date
from html import escape
from json import JSONDecodeError, loads as jloads
from markdown import Markdown
from pathlib import Path
from posixpath import relpath
from pygments.formatters import HtmlFormatter
from re import fullmatch
from shutil import rmtree
from sys import argv
from typing import Any
from urllib.parse import quote, unquote, urlsplit
from warnings import warn
import argparse

# constants
TEXT_EXTS = {'c', 'cpp', 'css', 'csv', 'h', 'hpp', 'htm', 'html', 'js', 'md', 'json', 'tsv', 'txt'}
IMAGE_EXTS = {'bmp', 'gif', 'ico', 'jpeg', 'jpg', 'png', 'svg', 'webp'}
HTTP_SCHEMES = {'http', 'https'}
MIMES = {
    'ico':  'image/x-icon',
    'png':  'image/png',
    'svg':  'image/svg+xml',
    'webp': 'image/webp',
}

REPO_ROOT_PATH = Path(argv[0]).expanduser().parent.parent.resolve()
REQUIRED_FRONTEND_FILES = (
    Path('style.css'),
    Path('site.js'),
    Path('social/github.svg'),
    Path('social/googlescholar.svg'),
    Path('social/linkedin.svg'),
    Path('social/orcid.svg'),
    Path('social/bluesky.svg'),
)
SOCIAL_PLATFORMS = (
    ('github', 'GitHub', 'github.svg'),
    ('google_scholar', 'Google Scholar', 'googlescholar.svg'),
    ('linkedin', 'LinkedIn', 'linkedin.svg'),
    ('orcid', 'ORCID', 'orcid.svg'),
    ('bluesky', 'Bluesky', 'bluesky.svg'),
)

# page builder: home
def build_home() -> str:
    biography_file = optional_site_match('biography', TEXT_EXTS, 'biography')
    biography_html = ''
    if biography_file is not None:
        biography = SITE.get(biography_file.name)
        if not isinstance(biography, str):
            raise TypeError(f"load_data() must return {biography_file} as a string.")
        suffix = biography_file.suffix.lower()
        if suffix == '.txt':
            biography_html = f'<p>{escape(biography)}</p>'
        elif suffix == '.md':
            biography_html = markdown_to_html(biography)
        elif suffix == '.html':
            biography_html = biography
        biography_html = f'<section class="biography">{biography_html}</section>'
    google_calendar_url = optional_site_text("google_calendar_url.txt")
    calendar_html = ''
    if google_calendar_url is not None:
        parsed_url = urlsplit(google_calendar_url)
        if parsed_url.scheme != "https" or parsed_url.hostname != "calendar.google.com" or parsed_url.path != "/calendar/embed":
            raise ValueError("site/google_calendar_url.txt must contain a Google Calendar embed URL (https://calendar.google.com/calendar/embed?...).")
        calendar_html = f'<section class="google-calendar"><iframe src="{escape(google_calendar_url, quote=True)}" title="Google Calendar" width="100%" height="600" loading="lazy" style="border: 0;"></iframe></section>'
    return biography_html + calendar_html

# page builder: research
def build_research(research_types=['papers', 'conferences', 'preprints']): # TODO add 'books', 'games'
    out_html = f'''<center>{' – '.join(f'<a href="#{research_type}">{translate(research_type)}</a>' for research_type in research_types)}</center>'''
    for research_type in research_types:
        research_html = dict() # research_html[year] = list of research type HTML values
        for entry_key, entry_meta in sorted(DATA['research'][research_type].items(), key=lambda x: x[1]['date.txt'], reverse=True):
            authors = list()
            for author_row in [l.strip() for l in entry_meta['authors.csv'].splitlines() if len(l.strip()) != 0]:
                first_name, last_name = [s.strip() for s in author_row.split(',')]
                abbrev_name = f"{last_name} {''.join(s[0] for s in first_name.replace('-',' ').split()).upper()}"
                if f'{first_name} {last_name}' == SITE_CONFIG['owner_name']:
                    authors.append(f'<b>{abbrev_name}</b>')
                else:
                    authors.append(abbrev_name)
            year = int(entry_meta['date.txt'].split('-')[0])
            if year not in research_html:
                research_html[year] = list()
            html = '<li>'
            html += f'''{', '.join(authors)} ({year}). "{entry_meta['title.txt']}." '''
            html += f'''<i>{entry_meta['venue.txt']}</i>. '''
            if 'volume.txt' in entry_meta:
                html += entry_meta['volume.txt']
            if 'issue.txt' in entry_meta:
                html += f"({entry_meta['issue.txt']})"
            if 'pages.txt' in entry_meta:
                if 'volume.txt' in entry_meta or 'issue.txt' in entry_meta:
                    html += ':'
                html += entry_meta['pages.txt'].replace('-','–')
            if 'volume.txt' in entry_meta or 'issue.txt' in entry_meta or 'pages.txt' in entry_meta:
                html += '.'
            if 'type.txt' in entry_meta:
                html += f" {entry_meta['type.txt']}."
            if 'url.txt' in entry_meta:
                html += f''' <a href="{entry_meta['url.txt']}" {external_link_attributes(True)}>Link</a>.'''
            if 'doi.txt' in entry_meta:
                html += f''' <a href="https://doi.org/{entry_meta['doi.txt']}" {external_link_attributes(True)}>doi:{entry_meta['doi.txt']}</a>'''
            if 'arxiv.txt' in entry_meta:
                html += f''' <a href="https://arxiv.org/abs/{entry_meta['arxiv.txt']}" {external_link_attributes(True)}>arXiv:{entry_meta['arxiv.txt']}</a>'''
            html = html.strip() + '</li>'
            research_html[year].append(html)
        list_start = dict(); curr_start = 0
        for year, htmls in sorted(research_html.items()):
            curr_start += len(htmls); list_start[year] = curr_start
        out_html += f'<h2 id="{research_type}">{translate(research_type)}</h2>'
        out_html += f'''<center>{' – '.join(f'<a href="#{research_type}-{year}">{year}</a>' for year in sorted(research_html.keys(), reverse=True))}</center>'''
        out_html += ''.join(f'''<h3 id="{research_type}-{year}">{year}</h3><ol reversed start={list_start[year]}>{''.join(htmls)}</ol><center>— <a href="#main-content">Top</a> —</center>''' for year, htmls in sorted(research_html.items(), reverse=True))
    return out_html

# page builder: students
def build_students():
    student_data = {k:v for k, v in DATA['students'].items() if not is_data_type(v)}
    student_html = dict() # student_html[year] = list of student HTML values
    for student_key, student_meta in sorted(student_data.items(), key=lambda x: x[1]['first_name.txt']):
        for k in ['first_name.txt', 'last_name.txt', 'start_year.txt', 'role.txt']:
            if k not in student_meta:
                raise ValueError(f"Student '{student_key}' is missing required metadata '{k}'")
        student_name = student_meta['first_name.txt'] + ' ' + student_meta['last_name.txt']
        start_year = int(student_meta['start_year.txt'])
        if 'end_year.txt' in student_meta:
            end_year = int(student_meta['end_year.txt'])
        else:
            end_year = date.today().year
        html = '<li>'
        if 'url.txt' in student_meta:
            html += f'''<a href="{student_meta['url.txt']}" {external_link_attributes(True)}><b>{student_name}</b></a>'''
        else:
            html += f'<b>{student_name}</b>'
        html += f" &mdash; {student_meta['role.txt']} "
        if 'advisor.txt' in student_meta:
            if 'advisor_url.txt' in student_meta:
                advisor_html = f'''<a href="{student_meta['advisor_url.txt']}" {external_link_attributes(True)}>{student_meta['advisor.txt']}</a>'''
            else:
                advisor_html = student_meta['advisor.txt']
            html += f"(Advisor: {advisor_html}) "
        if 'coadvisor.txt' in student_meta:
            if 'coadvisor_url.txt' in student_meta:
                coadvisor_html = f'''<a href="{student_meta['coadvisor_url.txt']}" {external_link_attributes(True)}>{student_meta['coadvisor.txt']}</a>'''
            else:
                coadvisor_html = student_meta['coadvisor.txt']
            html += f"(Co-Advisor: {coadvisor_html}) "
        html += f"({start_year}&ndash;{end_year})"
        html += '</li>'
        if end_year not in student_html:
            student_html[end_year] = list()
        student_html[end_year].append(html)
        out_html = f'<p>I have been <i>incredibly</i> fortunate to have gotten the opportunity to mentor such amazing graduate, undergraduate, and high school students. A complete list of my past students ({len(student_data)} total) can be found below.</p>'
        out_html += f'''<center>{' – '.join(f'<a href="#{year}">{year}</a>' for year in sorted(student_html.keys(), reverse=True))}</center>'''
        for year, htmls in sorted(student_html.items(), reverse=True):
            out_html += f'''<h2 id="{year}">{year}</h2><ul>{''.join(htmls)}</ul><center>— <a href="#main-content">Top</a> —</center>'''
    return out_html

# page builder functions TODO
PAGE_BUILDERS = {
    '': build_home,
    'research': build_research,
    'students': build_students,
}

# page order
PAGE_ORDER = {
    '': ['awards', 'research', 'students'],
    'research': ['papers', 'preprints'],
}

# copy a file
def copy_file(source_path, dest_path):
    with open(source_path, mode='rb') as in_f:
        with open(dest_path, mode='wb') as out_f:
            out_f.write(in_f.read())

# parse user args
def parse_args():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--input', required=False, type=str, default=REPO_ROOT_PATH, help="Root of GitHub Repository")
    parser.add_argument('-o', '--output', required=False, type=str, default=REPO_ROOT_PATH / 'html_out', help="Output Directory")
    parser.add_argument('--accent_color', required=False, type=str, default='#526D8A', help="Site Accent Color")
    parser.add_argument('--overwrite', required=False, type=str, choices=('yes', 'no', 'update'), default='no', help="Overwrite Output")
    args = parser.parse_args()
    args.input = Path(args.input)
    for p in (args.input, args.input / 'data', args.input / 'site'):
        if not p.is_dir():
            raise ValueError(f"Directory not found: {p}")
    args.output = Path(args.output)
    args.overwrite = args.overwrite.strip().lower()
    if args.output.exists():
        if args.overwrite == 'yes':
            rmtree(args.output)
        elif args.overwrite == 'no':
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

# translate key to human-readable label
def translate(label):
    if label in TRANSLATE:
        return TRANSLATE[label]
    return label.replace('_', ' ').title()

# convert Markdown to HTML
def markdown_to_html(source):
    converter = Markdown(
        extensions=['tables', 'fenced_code', 'footnotes', 'def_list', 'toc', 'codehilite'],
        extension_configs={
            'toc': {'permalink': True},
            'codehilite': {'guess_lang': False, 'use_pygments': True},
        },
    )
    return converter.convert(source)

# get relative directory URL
def page_url(target_folder, current_folder):
    target = target_folder.strip('/') or '.'
    current = current_folder.strip('/') or '.'
    relative = relpath(target, start=current)
    if relative == '.':
        relative = './'
    elif not relative.endswith('/'):
        relative += '/'
    return quote(relative, safe='/._-~')

# get relative asset URL
def asset_url(output_file, current_folder):
    if OUT_DIR is None:
        raise RuntimeError("OUT_DIR has not been initialized.")
    try:
        target_relative = output_file.relative_to(OUT_DIR).as_posix()
    except ValueError as exc:
        raise ValueError(f"Asset path must be inside OUT_DIR: {output_file}") from exc
    current = current_folder.strip('/') or '.'
    relative = relpath(target_relative, start=current)
    return quote(relative, safe='/._-~')

# render folder metadata alphabetically
def render_metadata(folder_path, current_folder):
    if current_folder is None:
        current_folder = folder_path
    folder = get_data_folder(folder_path)
    file_entries = sorted(((name, value) for name, value in folder.items() if not isinstance(value, dict)), key=lambda x: translate(Path(x[0]).stem).casefold())
    if not file_entries:
        return ''
    items = [f'<li><strong>{escape(translate(Path(name).stem))}:</strong> {render_data_value(name, value, folder_path, current_folder)}</li>' for name, value in file_entries]
    return f'<ul class="metadata-list">{"".join(items)}</ul>"'

# render child folder links
def render_child_folder_links(parent_folder, current_folder):
    children = ordered_child_folders(parent_folder)
    if not children:
        return ''
    items = list()
    for child_name in children:
        child_path = join_folder_key(parent_folder, child_name)
        href = page_url(child_path, current_folder)
        items.append(f'<li><a href="{escape(href, quote=True)}">{escape(translate(child_name))}</a></li>')
    return f'<ul class="child-folder-list">{"".join(items)}</ul>'

# get data folder
def get_data_folder(folder_path):
    folder = DATA
    if folder_path:
        for part in folder_path.split('/'):
            if not isinstance(folder, dict) or part not in folder:
                raise KeyError(f"No data folder named {folder_path!r}.")
            folder = folder[part]
    if not isinstance(folder, dict):
        raise TypeError(f"DATA entry {folder_path!r} is not a folder dictionary.")
    return folder

# join folder key
def join_folder_key(parent, child):
    return f"{parent}/{child}" if parent else child

# render data value
def render_data_value(filename, value, folder_path, current_folder):
    suffix = Path(filename).suffix.lower()
    source_file = REPO_ROOT_PATH / 'data' / Path(folder_path) / filename
    if suffix == '.txt':
        if not isinstance(value, str):
            raise TypeError(f"Expected text content for {source_file}.")
        return f'<span class="plain-value">{escape(value)}</span>'
    if suffix == '.md':
        if not isinstance(value, str):
            raise TypeError(f"Expected Markdown text content for {source_file}.")
        return markdown_to_html(value)
    if suffix == '.html':
        if not isinstance(value, str):
            raise TypeError(f"Expected HTML text content for {source_file}.")
        return value
    if not source_file.is_file():
        raise FileNotFoundError(f"DATA refers to a file that does not exist: {source_file}")
    destination = OUT_DIR / Path(folder_path) / filename
    destination.parent.mkdir(parents=True, exist_ok=True)
    copy_file(source_file, destination)
    href = asset_url(destination, current_folder)
    link_text = 'View file' if suffix in IMAGE_EXTS else 'Download'
    download_attribute = '' if suffix in IMAGE_EXTS else ' download'
    return f'<a href="{escape(href, quote=True)}"{download_attribute}>{link_text}</a>'

# validate runtime and sources
def validate_runtime_and_sources():
    if REPO_ROOT_PATH is None or OUT_DIR is None:
        raise RuntimeError("REPO_ROOT_PATH and OUT_DIR must be set before build_website().")
    if not REPO_ROOT_PATH.is_dir():
        raise FileNotFoundError(f"Repository root does not exist or is not a directory: {REPO_ROOT_PATH}")
    data_dir = REPO_ROOT_PATH / 'data'
    site_dir = REPO_ROOT_PATH / 'site'
    assets_dir = site_dir / 'assets'
    for p in (data_dir, site_dir):
        if not p.is_dir():
            raise FileNotFoundError(f"Critical source directory is missing: {p}")
    if not assets_dir.is_dir():
        raise FileNotFoundError(f"Critical frontend asset directory is missing: {assets_dir}")
    resolved_out = OUT_DIR.resolve()
    resolved_root = REPO_ROOT_PATH.resolve()
    resolved_data = data_dir.resolve()
    resolved_site = site_dir.resolve()
    if resolved_out == resolved_root or resolved_out.is_relative_to(resolved_data) or resolved_out.is_relative_to(resolved_site) or resolved_data.is_relative_to(resolved_out) or resolved_site.is_relative_to(resolved_out):
        raise ValueError(f"OUT_DIR must be separate from the repository root and must not overlap data/ or site/. Received OUT_DIR={resolved_out}.")
    missing_assets = [assets_dir / relative for relative in REQUIRED_FRONTEND_FILES if not (assets_dir / relative).is_file()]
    if missing_assets:
        raise FileNotFoundError(f"Required frontend asset files are missing:\n  {'\n  '.join(str(path) for path in missing_assets)}")
    if not fullmatch(r'#[0-9A-Fa-f]{6}', ACCENT_COLOR):
        raise ValueError(f"ACCENT_COLOR must be a six-digit hex color such as #526D8A, not {ACCENT_COLOR!r}.")

# load translations from /site/translate.json
def load_translations():
    source_file = REPO_ROOT_PATH / 'site' / 'translate.json'
    if source_file.is_file():
        value = SITE.get('translate.json')
        if not isinstance(value, str):
            raise TypeError(f"load_data() must return translate.json as a string: {source_file}")
        try:
            parsed = jloads(value)
        except JSONDecodeError as exc:
            raise ValueError(f"Invalid JSON in {source_file}: {exc}") from exc
        if not isinstance(parsed, dict) or any(not isinstance(key, str) or not isinstance(item, str) for key, item in parsed.items()):
            raise TypeError(f"{source_file} must contain a JSON object mapping strings to strings.")
        return parsed
    warn(f"Optional file not found: {source_file}; using Title Case fallback labels.", stacklevel=2)
    return dict()

# get optional site text
def optional_site_text(filename):
    source_file = REPO_ROOT_PATH / 'site' / filename
    if source_file.is_file():
        value = SITE.get(filename)
        if not isinstance(value, str):
            raise TypeError(f"load_data() must return {source_file} as a string.")
        value = value.strip()
        if not value:
            warn(f"Optional configuration file is empty: {source_file}", stacklevel=2)
            return None
        return value
    warn(f"Optional file not found: {source_file}", stacklevel=2)
    return None

# resolve site URL as (href, is_external, is_download) tuple
def resolve_site_url(value, *, config_file):
    parsed = urlsplit(value)
    if parsed.scheme or parsed.netloc:
        if parsed.scheme and parsed.scheme not in HTTP_SCHEMES:
            raise ValueError(f"Unsupported URL scheme in site/{config_file}: {value!r}")
        return value, True, False
    if not parsed.path:
        warn(f"Empty relative URL in site/{config_file}; omitting link.", stacklevel=2)
        return None
    relative_source = Path(unquote(parsed.path))
    if relative_source.is_absolute():
        raise ValueError(f"Relative site URLs must not be absolute filesystem paths ({config_file}: {value!r}).")
    site_root = REPO_ROOT_PATH / 'site'
    source_file = (site_root / relative_source).resolve()
    if not source_file.is_relative_to(site_root.resolve()):
        raise ValueError(f"Relative URL in site/{config_file} escapes the site/ directory: {value!r}")
    if source_file.is_file():
        relative = source_file.relative_to(site_root.resolve())
        destination = OUT_DIR / 'assets' / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        copy_file(source_file, destination)
        href = asset_url(destination, '')
        if parsed.query:
            href += '?' + parsed.query
        if parsed.fragment:
            href += '#' + parsed.fragment
        return href, False, True
    warn(f"File referenced by site/{config_file} was not found: {source_file}; omitting link.", stacklevel=2)
    return None

# optional site match
def optional_site_match(stem, allowed_extensions, label):
    site_dir = REPO_ROOT_PATH / 'site'
    matches = [path for path in site_dir.glob('*.*') if path.is_file() and path.stem == stem and path.suffix.lstrip('.').lower() in allowed_extensions]
    if len(matches) > 1:
        paths = ', '.join(str(path) for path in matches)
        raise ValueError(f"Multiple {label} files found; expected at most one: {paths}")
    if matches:
        return matches[0]
    warn(f"Optional {label} file not found in {site_dir}.", stacklevel=2)
    return None

# prepare site config
def prepare_site_config():
    global SITE_CONFIG
    first_name = optional_site_text('first_name.txt')
    last_name = optional_site_text('last_name.txt')
    owner_name = ' '.join(part for part in (first_name, last_name) if part)
    site_title = optional_site_text('title.txt') or owner_name or 'Academic Website'
    position = optional_site_text('position.txt')
    department = optional_site_text('department.txt')
    institution = optional_site_text('institution.txt')
    email = optional_site_text('email.txt')
    site_root = (REPO_ROOT_PATH / 'site').resolve()
    photo_source = optional_site_match('photo', IMAGE_EXTS, 'profile photo')
    photo_destination = None
    if photo_source is not None:
        photo_source = photo_source.resolve()
        if not photo_source.is_relative_to(site_root):
            raise ValueError(f"Profile photo must be inside {site_root}: {photo_source}")
        photo_destination = OUT_DIR / 'assets' / photo_source.relative_to(site_root)
        photo_destination.parent.mkdir(parents=True, exist_ok=True)
        copy_file(photo_source, photo_destination)
    favicon_source = optional_site_match('favicon', IMAGE_EXTS, 'favicon')
    favicon_destination = None
    if favicon_source is not None:
        favicon_source = favicon_source.resolve()
        if not favicon_source.is_relative_to(site_root):
            raise ValueError(f"Favicon must be inside {site_root}: {favicon_source}")
        favicon_destination = OUT_DIR / 'assets' / favicon_source.relative_to(site_root)
        favicon_destination.parent.mkdir(parents=True, exist_ok=True)
        copy_file(favicon_source, favicon_destination)
    cv_value = optional_site_text('cv_url.txt')
    cv_link = resolve_site_url(cv_value, config_file='cv_url.txt') if cv_value else None
    social_links = list()
    for key, label, icon_name in SOCIAL_PLATFORMS:
        config_name = f"{key}_url.txt"
        value = optional_site_text(config_name)
        if value:
            resolved = resolve_site_url(value, config_file=config_name)
            if resolved:
                href, is_external, is_download = resolved
                social_links.append({
                    'label': label,
                    'icon': OUT_DIR / 'assets' / 'social' / icon_name,
                    'href': href,
                    'external': is_external,
                    'download': is_download,
                })
    footer_candidates = [path for path in (REPO_ROOT_PATH / 'site').iterdir() if path.is_file() and path.stem == 'footer']
    if len(footer_candidates) > 1:
        raise ValueError(f"Only one site/footer.* file is allowed: {', '.join(str(path) for path in footer_candidates)}")
    footer_html = ''
    if footer_candidates:
        footer_file = footer_candidates[0]
        footer_value = SITE.get(footer_file.name)
        if not isinstance(footer_value, str):
            raise TypeError(f"load_data() must return {footer_file} as a string.")
        if footer_file.suffix.lower() == '.txt':
            footer_html = f"<p>{escape(footer_value)}</p>"
        elif footer_file.suffix.lower() == '.md':
            footer_html = markdown_to_html(footer_value)
        elif footer_file.suffix.lower() == '.html':
            footer_html = footer_value
        else:
            warn(f"Unrecognized footer extension in {footer_file}; using the default footer.", stacklevel=2)
            footer_html = f"<p>{escape(f'© {date.today().year} {owner_name}'.strip())}</p>"
        footer_html = footer_html.replace('{year}', str(date.today().year))
        footer_html = footer_html.replace('{name}', escape(owner_name))
    else:
        warn(f"Optional footer file not found in {REPO_ROOT_PATH / 'site'}; using the default footer.", stacklevel=2)
        default_footer = f"© {date.today().year} {owner_name}".strip()
        footer_html = f"<p>{escape(default_footer)}</p>"
    SITE_CONFIG = {
        'owner_name': owner_name,
        'site_title': site_title,
        'position': position,
        'department': department,
        'institution': institution,
        'email': email,
        'photo_path': photo_destination,
        'favicon_path': favicon_destination,
        'cv_link': cv_link,
        'social_links': social_links,
        'footer_html': footer_html,
    }

# check if a given folder is a data type (rather than a data entry)
def is_data_type(folder):
    return any(isinstance(v, dict) for v in folder.values())

# iterate over folder paths
def iter_folder_paths(folder=None, parent=''):
    if folder is None:
        folder = DATA
    for k, v in folder.items():
        if not isinstance(v, dict) or not is_data_type(v):
            continue
        path = join_folder_key(parent, k)
        yield path
        yield from iter_folder_paths(v, path)

# validate duplicate stems
def validate_duplicate_stems(folder, folder_path=''):
    stems = dict()
    for name, value in folder.items():
        if isinstance(value, dict):
            validate_duplicate_stems(value, join_folder_key(folder_path, name)); continue
        stem = Path(name).stem
        if stem in stems:
            raise ValueError(f"Duplicate metadata filename stem {stem!r} in data/{folder_path}: {stems[stem]!r} and {name!r}.")
        stems[stem] = name

# validate page configuration
def validate_page_configuration():
    folder_paths = {'', *iter_folder_paths()}
    for folder_path, builder in PAGE_BUILDERS.items():
        if not isinstance(folder_path, str):
            raise TypeError(f"PAGE_BUILDERS keys must be strings, not {type(folder_path).__name__}.")
        if folder_path not in folder_paths:
            warn(f"PAGE_BUILDERS refers to a folder that does not exist: {folder_path!r}.", stacklevel=2)
        if not callable(builder):
            raise TypeError(f"PAGE_BUILDERS[{folder_path!r}] must be a callable zero-argument function.")
    for parent_path, ordered_names in PAGE_ORDER.items():
        if not isinstance(parent_path, str):
            raise TypeError(f"PAGE_ORDER keys must be strings, not {type(parent_path).__name__}.")
        if not isinstance(ordered_names, list) or any(not isinstance(name, str) for name in ordered_names):
            raise TypeError(f"PAGE_ORDER[{parent_path!r}] must be a list of child-folder strings.")
        if parent_path not in folder_paths:
            warn(f"PAGE_ORDER refers to a parent folder that does not exist: {parent_path!r}.", stacklevel=2)
            continue
        child_folders = {name for name, value in get_data_folder(parent_path).items() if isinstance(value, dict)}
        seen = set()
        for child_name in ordered_names:
            if child_name not in child_folders:
                warn(f"PAGE_ORDER entry does not exist: {parent_path!r} -> {child_name!r}; ignoring it.", stacklevel=2)
            elif child_name in seen:
                warn(f"Duplicate PAGE_ORDER entry: {parent_path!r} -> {child_name!r}; ignoring the duplicate.", stacklevel=2)
            seen.add(child_name)

# get ordered child folders
def ordered_child_folders(parent_path):
    folder = get_data_folder(parent_path)
    child_names = [name for name, value in folder.items() if isinstance(value, dict)]
    configured = PAGE_ORDER.get(parent_path, list())
    valid_configured = [name for name in configured if name in child_names]
    listed = set(valid_configured)
    unlisted = sorted((name for name in child_names if name not in listed), key=lambda name: translate(name).casefold())
    return valid_configured + unlisted

# validate loaded tree
def validate_loaded_tree(tree, source_label):
    for name, value in tree.items():
        if not isinstance(name, str):
            raise TypeError(f"{source_label} dictionary keys must be strings, not {type(name).__name__}.")
        if isinstance(value, dict):
            validate_loaded_tree(value, f"{source_label}/{name}")
        elif value is not None and not isinstance(value, str):
            raise TypeError(f"{source_label}/{name} must be a text string, a nested directory dictionary, or None for binary files.")

# validate data tree
def validate_data_tree():
    if not isinstance(DATA, dict):
        raise TypeError("load_data(path=.../data) must return a nested dictionary.")
    if not isinstance(SITE, dict):
        raise TypeError("load_data(path=.../site) must return a nested dictionary.")
    validate_loaded_tree(DATA, 'data')
    validate_loaded_tree(SITE, 'site')
    validate_duplicate_stems(DATA)

# render generic page body
def render_generic_body(folder_path):
    metadata_html = render_metadata(folder_path, folder_path)
    children_html = render_child_folder_links(folder_path, folder_path)
    parts = list()
    if metadata_html:
        parts.append(metadata_html)
    if children_html:
        parts.append(f'<section class="child-folders"><h2>Contents</h2>{children_html}</section>')
    return ''.join(parts)

# render breadcrumbs
def render_breadcrumbs(folder_path):
    if not folder_path:
        return ''
    parts = ['<nav class="breadcrumbs" aria-label="Breadcrumb">', '<ol>', f'<li><a href="{escape(page_url("", folder_path), quote=True)}">Home</a></li>']
    ancestors = list()
    current = ''
    for segment in folder_path.split('/'):
        current = join_folder_key(current, segment)
        ancestors.append(current)
    for index, ancestor in enumerate(ancestors):
        label = translate(ancestor.rsplit('/', 1)[-1])
        if index == len(ancestors) - 1:
            parts.append(f'<li aria-current="page"><span>{escape(label)}</span></li>')
        else:
            href = page_url(ancestor, folder_path)
            parts.append(f'<li><a href="{escape(href, quote=True)}">{escape(label)}</a></li>')
    parts.append('</ol></nav>')
    return ''.join(parts)

# render sidebar navigation
def render_sidebar_navigation(current_folder):
    items = list()
    for name in [''] + ordered_child_folders(''):
        href = page_url(name, current_folder)
        active = current_folder == name
        is_ancestor = bool(name) and current_folder.startswith(name + '/')
        active_class = ' active' if active else (' ancestor' if is_ancestor else '')
        current_attr = ' aria-current="page"' if active else ''
        label = 'Home' if name == '' else escape(translate(name))
        items.append(f'<li class="nav-item"><div class="nav-row"><a class="nav-link{active_class}" href="{escape(href, quote=True)}"{current_attr}>{label}</a></div></li>')
    return f'<nav class="sidebar-nav" aria-label="Site navigation"><ul class="nav-tree">{"".join(items)}</ul></nav>'

# render top navigation
def render_top_navigation(current_folder):
    items = list()
    for name in [''] + ordered_child_folders(''):
        href = page_url(name, current_folder)
        active = current_folder == name or current_folder.startswith(name + '/')
        active_class = ' active' if active else ''
        current_attr = ' aria-current="location"' if active else ''
        items.append(f'<li><a class="top-nav-link{active_class}" href="{escape(href, quote=True)}"{current_attr}>{"Home" if name == "" else escape(translate(name))}</a></li>')
    return f'<nav class="top-navigation" aria-label="Top-level navigation"><ul>{"".join(items)}</ul></nav>'

# external link attributes
def external_link_attributes(is_external):
    return ' target="_blank" rel="noopener noreferrer"' if is_external else ''

# render profile
def render_profile(current_folder):
    owner_name = SITE_CONFIG['owner_name']
    photo = SITE_CONFIG['photo_path']
    photo_html = ''
    if photo:
        photo_href = asset_url(photo, current_folder)
        photo_html = (f'<img class="profile-photo" src="{escape(photo_href, quote=True)}" alt="{escape(owner_name or "Profile photo", quote=True)}">')
    identity_parts = list()
    if owner_name:
        identity_parts.append(f'<div class="profile-name">{escape(owner_name)}</div>')
    if SITE_CONFIG['position']:
        identity_parts.append(f'<div class="profile-position">{escape(SITE_CONFIG["position"])}</div>')
    if SITE_CONFIG['department']:
        identity_parts.append(f'<div class="profile-department">{escape(SITE_CONFIG["department"])}</div>')
    if SITE_CONFIG['institution']:
        identity_parts.append(f'<div class="profile-institution">{escape(SITE_CONFIG["institution"])}</div>')
    contact_parts = list()
    if SITE_CONFIG['email']:
        email_value = SITE_CONFIG['email']
        contact_parts.append(f'<a class="profile-email" href="mailto:{escape(email_value, quote=True)}">{escape(email_value)}</a>')
    if SITE_CONFIG['cv_link']:
        href, is_external, is_download = SITE_CONFIG['cv_link']
        download = ' download' if is_download else ''
        contact_parts.append(f'<a class="profile-cv" href="{escape(href, quote=True)}"{external_link_attributes(is_external)}{download}>Download CV</a>')
    social_parts = list()
    for social in SITE_CONFIG['social_links']:
        icon_href = asset_url(social['icon'], current_folder)
        social_parts.append(f'<a class="social-link" href="{escape(social["href"], quote=True)}" aria-label="{escape(social["label"], quote=True)}"{external_link_attributes(social["external"])}><img src="{escape(icon_href, quote=True)}" alt="" loading="lazy"></a>')
    return f'{photo_html}<div class="profile-identity">{"".join(identity_parts)}</div><div class="profile-contact">{"".join(contact_parts)}</div>' + ('<div class="social-links" aria-label="Social links">' + "".join(social_parts) + "</div>" if social_parts else "")

# render a page
def render_page(folder_path, body_html):
    heading = SITE_CONFIG['site_title'] if not folder_path else translate(folder_path.rsplit('/', 1)[-1])
    owner_name = SITE_CONFIG['owner_name']
    if not folder_path:
        document_title = heading
    else:
        document_title = f"{heading} | {owner_name}" if owner_name else heading
    stylesheet_href = asset_url(OUT_DIR / 'assets' / 'style.css', folder_path)
    pygments_href = asset_url(OUT_DIR / 'assets' / 'pygments.css', folder_path)
    script_href = asset_url(OUT_DIR / 'assets' / 'site.js', folder_path)
    favicon_html = ''
    if SITE_CONFIG['favicon_path']:
        favicon_path = SITE_CONFIG['favicon_path']
        favicon_href = asset_url(favicon_path, folder_path)
        mime = MIMES.get(favicon_path.suffix.lower(), 'image/x-icon')
        favicon_html = f'<link rel="icon" href="{escape(favicon_href, quote=True)}" type="{mime}">'
    profile_html = render_profile(folder_path)
    sidebar_nav = render_sidebar_navigation(folder_path)
    top_nav = render_top_navigation(folder_path)
    breadcrumbs = render_breadcrumbs(folder_path)
    footer_html = SITE_CONFIG['footer_html']
    accent = escape(ACCENT_COLOR, quote=True)
    mobile_photo = ''
    if SITE_CONFIG['photo_path']:
        mobile_photo_href = asset_url(SITE_CONFIG['photo_path'], folder_path)
        mobile_photo = f'<img class="mobile-profile-photo" src="{escape(mobile_photo_href, quote=True)}" alt="" loading="lazy">'
    mobile_name = escape(owner_name or SITE_CONFIG['site_title'])
    return f'<!doctype html><html lang="en" style="--accent-color: {accent}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="color-scheme" content="light dark"><title>{escape(document_title)}</title>{favicon_html}<link rel="stylesheet" href="{escape(stylesheet_href, quote=True)}"><link rel="stylesheet" href="{escape(pygments_href, quote=True)}"><script src="{escape(script_href, quote=True)}" defer></script></head><body><a class="skip-link" href="#main-content">Skip to main content</a><div class="site-layout"><aside class="site-sidebar" id="site-sidebar" aria-label="Profile and site navigation"><div class="sidebar-inner"><div class="sidebar-mobile-controls"><span class="sidebar-menu-label">Menu</span><button class="sidebar-close" id="sidebar-close" type="button" aria-label="Close navigation">×</button></div><section class="profile-panel" aria-label="Profile">{profile_html}</section><div class="sidebar-tools"><button class="theme-toggle theme-toggle-desktop" type="button" data-theme-toggle><span class="theme-toggle-label">Change theme</span></button></div>{sidebar_nav}</div></aside><button class="sidebar-backdrop" id="sidebar-backdrop" type="button" aria-label="Close navigation" tabindex="-1"></button><div class="main-column"><header class="mobile-header"><div class="mobile-identity">{mobile_photo}<span>{mobile_name}</span></div><div class="mobile-header-actions"><button class="theme-toggle theme-toggle-mobile" type="button" data-theme-toggle aria-label="Change color theme">Theme</button><button class="mobile-menu-button" id="mobile-menu-button" type="button" aria-controls="site-sidebar" aria-expanded="false" aria-label="Open navigation"><span></span><span></span><span></span></button></div></header>{top_nav}<main id="main-content" class="main-content" tabindex="-1"><div class="content-narrow page-heading">{breadcrumbs}<h1>{escape(heading)}</h1></div><div class="content-body">{body_html}</div></main><footer class="site-footer"><div class="content-narrow">{footer_html}</div></footer></div></div></body></html>'

# copy frontend assets to output folder
def copy_frontend_assets():
    source_assets = REPO_ROOT_PATH / 'site' / 'assets'
    destination_assets = OUT_DIR / 'assets'
    destination_assets.mkdir(parents=True, exist_ok=True)
    for source in sorted(source_assets.rglob('*')):
        relative = source.relative_to(source_assets)
        destination = destination_assets / relative
        if source.is_dir():
            destination.mkdir(parents=True, exist_ok=True)
        elif source.is_file():
            destination.parent.mkdir(parents=True, exist_ok=True)
            copy_file(source, destination)
        else:
            warn(f"Skipping non-file frontend asset: {source}", stacklevel=2)

# write pygments stylesheet
def write_pygments_stylesheet():
    light_css = HtmlFormatter(style='friendly').get_style_defs('.codehilite')
    dark_css = HtmlFormatter(style='monokai').get_style_defs('html[data-theme="dark"] .codehilite')
    stylesheet = f"{light_css}\n{dark_css}"
    destination = OUT_DIR / 'assets' / 'pygments.css'
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(stylesheet, encoding='utf-8')

# build all pages
def build_all_pages():
    folder_paths = ['', *iter_folder_paths()]
    for folder_path in folder_paths:
        builder = PAGE_BUILDERS.get(folder_path)
        if builder is not None:
            body_html = builder()
            if not isinstance(body_html, str):
                raise TypeError(f"Custom builder for {folder_path!r} must return an HTML string; got {type(body_html).__name__}.")
        else:
            warn(f"No custom page builder is registered for {folder_path!r}.", stacklevel=2)
            continue
        page_directory = OUT_DIR / Path(folder_path)
        page_directory.mkdir(parents=True, exist_ok=True)
        output_file = page_directory / 'index.html'
        output_file.write_text(render_page(folder_path, body_html), encoding='utf-8')

# build website
def build_website():
    validate_runtime_and_sources()
    validate_data_tree()
    global TRANSLATE; TRANSLATE = load_translations()
    validate_page_configuration()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    copy_frontend_assets()
    prepare_site_config()
    write_pygments_stylesheet()
    build_all_pages()

# main logic
def main():
    global REPO_ROOT_PATH, OUT_DIR, DATA, SITE, ACCENT_COLOR
    args = parse_args()
    REPO_ROOT_PATH = args.input
    OUT_DIR = args.output
    ACCENT_COLOR = args.accent_color
    DATA = load_data(path=REPO_ROOT_PATH / 'data')
    SITE = load_data(path=REPO_ROOT_PATH / 'site')
    build_website()

# run script
if __name__ == '__main__':
    main()
