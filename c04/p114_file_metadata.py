import os
import time

from c02.p044_humansize import approximate_size

print(os.getcwd())
metadata = os.stat('p113_glob.py')
print(metadata.st_mtime)
print(time.localtime(metadata.st_mtime))

print()
print(metadata.st_size)
print(approximate_size(metadata.st_size))

print()
print(os.path.realpath('p113_glob.py'))

"""
/Users/moqi/Documents/Code/dive-into-python3-practice/c04
1587258259.9039261
time.struct_time(tm_year=2020, tm_mon=4, tm_mday=19, tm_hour=9, tm_min=4, tm_sec=19, tm_wday=6, tm_yday=110, tm_isdst=0)

890
0.9 KiB

/Users/moqi/Documents/Code/dive-into-python3-practice/c04/p113_glob.py
"""
