import pickle
import time

from file_path_collect import output_pickle_path_dir as output

shell = 1

entry = {'title': 'Divve into history, 2009 edition',
         'article_link': 'http://diveintomark.org/archives/2009/03/27/dive‐into‐history‐2009‐edition',
         'comments_link': None, 'internal_id': b'\xDE\xD5\xB4\xF8', 'tags': ('diveintopython', 'docbook', 'html'),
         'published': True, 'published_date': time.strptime('Fri Mar 27 22:20:42 2009')}

print(entry['published_date'])

with open(output + 'entry.pickle', 'wb') as f:
    pickle.dump(entry, f)
print('pickle save done.')
print()

# 序列化到内存中
b = pickle.dumps(entry)
print(type(b))
entry3 = pickle.loads(b)
print(entry == entry3)

"""
time.struct_time(tm_year=2009, tm_mon=3, tm_mday=27, tm_hour=22, tm_min=20, tm_sec=42, tm_wday=4, tm_yday=86, tm_isdst=-1)
pickle save done.

<class 'bytes'>
True
"""
