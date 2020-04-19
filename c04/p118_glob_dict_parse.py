import glob
import os
import pprint

from c02.p044_humansize import approximate_size

os.chdir('../resource/output')
glob_png = glob.glob('*.png')
pprint.pprint(glob_png)

print()
metadata = [(f, os.stat(f)) for f in glob_png]
pprint.pprint(metadata[0])

print()
dic_metadata = {f: os.stat(f) for f in glob_png}
print(type(dic_metadata))

print()
pprint.pprint(dic_metadata['catlogo.png'])

print()
pprint.pprint(list(dic_metadata.keys()))
print()
pprint.pprint(dic_metadata['catlogo.png'].st_size)

print()
humansize_dict = {os.path.splitext(f)[0]: approximate_size(meta.st_size)
                  for f, meta in dic_metadata.items() if meta.st_size > 600000}
pprint.pprint(humansize_dict)

"""
['rotate180.png',
 'cropped.png',
 'rotete6_expanded.png',
 'quartersized.png',
 'rotete6.png',
 'rotate90.png',
 'putPixel.png',
 'catlogo.png',
 'rotate270.png',
 'transparentImage.png',
 'pasted.png',
 'tiled.png',
 'purpleImage.png',
 'horizontal_flip.png',
 'svelte.png',
 'vertical_flip.png']

('rotate180.png',
 os.stat_result(st_mode=33188, st_ino=75106753, st_dev=16777220, st_nlink=1, st_uid=502, st_gid=20, st_size=1412931, st_atime=1587260921, st_mtime=1586738794, st_ctime=1587260921))

<class 'dict'>

os.stat_result(st_mode=33188, st_ino=75106748, st_dev=16777220, st_nlink=1, st_uid=502, st_gid=20, st_size=16726, st_atime=1587261009, st_mtime=1411527910, st_ctime=1587260921)

['rotate180.png',
 'cropped.png',
 'rotete6_expanded.png',
 'quartersized.png',
 'rotete6.png',
 'rotate90.png',
 'putPixel.png',
 'catlogo.png',
 'rotate270.png',
 'transparentImage.png',
 'pasted.png',
 'tiled.png',
 'purpleImage.png',
 'horizontal_flip.png',
 'svelte.png',
 'vertical_flip.png']

16726

{'horizontal_flip': '1.3 MiB',
 'pasted': '1.4 MiB',
 'rotate180': '1.3 MiB',
 'rotate270': '1.1 MiB',
 'rotate90': '1.1 MiB',
 'rotete6': '1.3 MiB',
 'rotete6_expanded': '1.4 MiB',
 'svelte': '1.6 MiB',
 'vertical_flip': '1.3 MiB'}
"""
