from c02.p044_humansize import SUFFIXES

print(len(SUFFIXES))
print(1000 in SUFFIXES)
print(SUFFIXES[1000])
print(SUFFIXES[1024])
print(SUFFIXES[1024][3])

"""
2
True
['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']
TiB
"""
