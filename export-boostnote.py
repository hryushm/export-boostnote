#!/usr/bin/env python3
import sys
import json
import re
import os.path
from argparse import ArgumentParser
from datetime import datetime as dt

#arguments setting
usage = 'Usage: ./export-boostnote.py [--date]'
parser = ArgumentParser(usage=usage)
parser.add_argument('path_to_data', \
        action='store', \
        nargs=None, \
        help='Path to Boostnote data to export (data.json)' )
parser.add_argument('-d', '--date', \
        action='store_true', \
        default=False, \
        help='export markdown file name with created date. e.g. "yymmdd_FILENAME"')
args = parser.parse_args()

MDDIR = './markdown/'
SNDIR = './snippets/'
DATE_PATTERN = r"\d{4}-\d{2}-\d{2}"

if not os.path.exists(MDDIR):
    os.mkdir(MDDIR)
if not os.path.exists(SNDIR):
    os.mkdir(SNDIR)

notes = json.load(open(args.path_to_data))['notes']

for note in notes :

    if note['type'] == 'MARKDOWN_NOTE':
        filename = note['title'] + '.md'
        if args.date:
            datetime = re.match(DATE_PATTERN, note['createdAt'])
            ymd = dt.strptime(datetime.group(), '%Y-%m-%d').strftime('%y%m%d')
            filename = ymd + '_' + filename
        print(filename)
        open(MDDIR + filename, 'w').write(note['content'])

    if note['type'] == 'SNIPPET_NOTE':
        for snippet in note['snippets']:
            filename = snippet['name']
            print(filename)
            open(SNDIR + filename, 'w').write(snippet['content'])
