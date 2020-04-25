import time

shell = 1

entry = {}

entry['title'] = 'Divve into history, 2009 edition'
entry['article_link'] = 'http://diveintomark.org/archives/2009/03/27/dive‐into‐history‐2009‐edition'
entry['comments_link'] = None
entry['internal_id'] = b'\xDE\xD5\xB4\xF8'
entry['tags'] = ('diveintopython', 'docbook', 'html')
entry['published'] = True
entry['published_date'] = time.strptime('Fri Mar 27 22:20:42 2009')

print(entry['published_date'])

"""
time.struct_time(tm_year=2009, tm_mon=3, tm_mday=27, tm_hour=22, tm_min=20, tm_sec=42, tm_wday=4, tm_yday=86, tm_isdst=-1)
"""
