import json
import pickle
from pprint import pprint

from file_path_collect import output_pickle_path_dir as output, output_json_path_dir as json_output

with open(output + 'entry.pickle', 'rb') as f:
    entry = pickle.load(f)

pprint(entry)

with open(json_output + 'entry.json', 'w', encoding='utf-8') as f:
    json.dump(entry, f)

"""
Traceback (most recent call last):
  File "/Users/moqi/Code/dive-into-python3-practice/c14/p413_json_wrong.py", line 13, in <module>
    json.dump(entry, f)
  File "/usr/local/Cellar/python/3.7.7/Frameworks/Python.framework/Versions/3.7/lib/python3.7/json/__init__.py", line 179, in dump
    for chunk in iterable:
  File "/usr/local/Cellar/python/3.7.7/Frameworks/Python.framework/Versions/3.7/lib/python3.7/json/encoder.py", line 431, in _iterencode
    yield from _iterencode_dict(o, _current_indent_level)
  File "/usr/local/Cellar/python/3.7.7/Frameworks/Python.framework/Versions/3.7/lib/python3.7/json/encoder.py", line 405, in _iterencode_dict
    yield from chunks
  File "/usr/local/Cellar/python/3.7.7/Frameworks/Python.framework/Versions/3.7/lib/python3.7/json/encoder.py", line 438, in _iterencode
    o = _default(o)
  File "/usr/local/Cellar/python/3.7.7/Frameworks/Python.framework/Versions/3.7/lib/python3.7/json/encoder.py", line 179, in default
    raise TypeError(f'Object of type {o.__class__.__name__} '
TypeError: Object of type bytes is not JSON serializable
{'article_link': 'http://diveintomark.org/archives/2009/03/27/dive‐into‐history‐2009‐edition',
 'comments_link': None,
 'internal_id': b'\xde\xd5\xb4\xf8',
 'published': True,
 'published_date': time.struct_time(tm_year=2009, tm_mon=3, tm_mday=27, tm_hour=22, tm_min=20, tm_sec=42, tm_wday=4, tm_yday=86, tm_isdst=-1),
 'tags': ('diveintopython', 'docbook', 'html'),
 'title': 'Divve into history, 2009 edition'}
"""
