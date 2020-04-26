import json
from pprint import pprint

from c14.p422_customerializer3 import from_json
from file_path_collect import output_json_path_dir as out

with open(out + 'entry.json', 'r', encoding='utf-8') as f:
    entry = json.load(f, object_hook=from_json)

pprint(entry)

"""
{'article_link': 'http://diveintomark.org/archives/2009/03/27/dive‐into‐history‐2009‐edition',
 'comments_link': None,
 'internal_id': b'\xde\xd5\xb4\xf8',
 'published': True,
 'published_date': [2009, 3, 27, 22, 20, 42, 4, 86, -1],
 'tags': ['diveintopython', 'docbook', 'html'],
 'title': 'Divve into history, 2009 edition'}
"""
