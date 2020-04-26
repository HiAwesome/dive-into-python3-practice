import json
from pprint import pprint

from file_path_collect import output_json_path_dir as json_output

with open(json_output + 'entry.json', 'r', encoding='utf-8') as f:
    entry = json.load(f)

pprint(entry)

"""
{'article_link': 'http://diveintomark.org/archives/2009/03/27/dive‐into‐history‐2009‐edition',
 'comments_link': None,
 'internal_id': {'__class__': 'bytes', '__value__': [222, 213, 180, 248]},
 'published': True,
 'published_date': [2009, 3, 27, 22, 20, 42, 4, 86, -1],
 'tags': ['diveintopython', 'docbook', 'html'],
 'title': 'Divve into history, 2009 edition'}
"""
