import json
import time

from c14.p415_customerializer import to_json
from file_path_collect import output_json_path_dir as json_output

entry = {'title': 'Divve into history, 2009 edition',
         'article_link': 'http://diveintomark.org/archives/2009/03/27/dive‐into‐history‐2009‐edition',
         'comments_link': None, 'internal_id': b'\xDE\xD5\xB4\xF8', 'tags': ('diveintopython', 'docbook', 'html'),
         'published': True, 'published_date': time.strptime('Fri Mar 27 22:20:42 2009')}

with open(json_output + 'entry.json', 'w', encoding='utf-8') as f:
    # time 对象现在已经可以被 dump 了，是一个 int 数组˚
    json.dump(entry, f, default=to_json)

"""
{'article_link': 'http://diveintomark.org/archives/2009/03/27/dive‐into‐history‐2009‐edition',
 'comments_link': None,
 'internal_id': b'\xde\xd5\xb4\xf8',
 'published': True,
 'published_date': time.struct_time(tm_year=2009, tm_mon=3, tm_mday=27, tm_hour=22, tm_min=20, tm_sec=42, tm_wday=4, tm_yday=86, tm_isdst=-1),
 'tags': ('diveintopython', 'docbook', 'html'),
 'title': 'Divve into history, 2009 edition'}
"""
