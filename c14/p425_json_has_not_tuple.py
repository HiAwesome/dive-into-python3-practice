import json
import time
from pprint import pprint

from p422_customerializer3 import to_json, from_json
from file_path_collect import output_json_path_dir as json_output

entry = {'title': 'Divve into history, 2009 edition',
         'article_link': 'http://diveintomark.org/archives/2009/03/27/dive‐into‐history‐2009‐edition',
         'comments_link': None, 'internal_id': b'\xDE\xD5\xB4\xF8', 'tags': ('diveintopython', 'docbook', 'html'),
         'published': True, 'published_date': time.strptime('Fri Mar 27 22:20:42 2009')}

with open(json_output + 'entry.json', 'w', encoding='utf-8') as f:
    json.dump(entry, f, default=to_json)

with open(json_output + 'entry.json', 'r', encoding='utf-8') as f:
    parse_entry = json.load(f, object_hook=from_json)

print(entry == parse_entry)
pprint(entry['tags'])
pprint(parse_entry['tags'])

"""
False
('diveintopython', 'docbook', 'html')
['diveintopython', 'docbook', 'html']
"""
