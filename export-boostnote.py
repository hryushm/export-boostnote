#!/usr/bin/env python3
import sys
import json
import re
from datetime import datetime as dt

MDDIR = './markdown/'
SNDIR = './snippets/'
DATE_PATTERN = r"\d{4}-\d{2}-\d{2}"

notes = json.load(open(sys.argv[1]))['notes']

for note in notes :
    datetime = re.match(DATE_PATTERN, note['createdAt'])
    ymd = dt.strptime(datetime.group(), '%Y-%m-%d').strftime('%y%m%d')

    if note['type'] == 'MARKDOWN_NOTE':
        filename = ymd + '_' + note['title'] + '.md'
        print(filename)
        open(MDDIR + filename, 'w').write(note['content'])

    if note['type'] == 'SNIPPET_NOTE':
        for snippet in note['snippets']:
            filename = snippet['name']
            print(filename)
            open(SNDIR + filename, 'w').write(snippet['content'])
