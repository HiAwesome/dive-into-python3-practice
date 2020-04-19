import glob
import os
import pprint

from c02.p044_humansize import approximate_size

os.chdir('../resource/output')
glob_png = glob.glob('*.png')

pprint.pprint(glob_png)

print()
pprint.pprint([os.path.realpath(f) for f in glob_png])

print()
pprint.pprint([f for f in glob_png if os.stat(f).st_size > 600000])

print()
pprint.pprint([(os.stat(f).st_size, os.path.realpath(f)) for f in glob_png])

print()
pprint.pprint([(approximate_size(os.stat(f).st_size), f) for f in glob_png])

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

['/Users/moqi/Documents/Code/dive-into-python3-practice/resource/output/rotate180.png',
 '/Users/moqi/Documents/Code/dive-into-python3-practice/resource/output/cropped.png',
 '/Users/moqi/Documents/Code/dive-into-python3-practice/resource/output/rotete6_expanded.png',
 '/Users/moqi/Documents/Code/dive-into-python3-practice/resource/output/quartersized.png',
 '/Users/moqi/Documents/Code/dive-into-python3-practice/resource/output/rotete6.png',
 '/Users/moqi/Documents/Code/dive-into-python3-practice/resource/output/rotate90.png',
 '/Users/moqi/Documents/Code/dive-into-python3-practice/resource/output/putPixel.png',
 '/Users/moqi/Documents/Code/dive-into-python3-practice/resource/output/catlogo.png',
 '/Users/moqi/Documents/Code/dive-into-python3-practice/resource/output/rotate270.png',
 '/Users/moqi/Documents/Code/dive-into-python3-practice/resource/output/transparentImage.png',
 '/Users/moqi/Documents/Code/dive-into-python3-practice/resource/output/pasted.png',
 '/Users/moqi/Documents/Code/dive-into-python3-practice/resource/output/tiled.png',
 '/Users/moqi/Documents/Code/dive-into-python3-practice/resource/output/purpleImage.png',
 '/Users/moqi/Documents/Code/dive-into-python3-practice/resource/output/horizontal_flip.png',
 '/Users/moqi/Documents/Code/dive-into-python3-practice/resource/output/svelte.png',
 '/Users/moqi/Documents/Code/dive-into-python3-practice/resource/output/vertical_flip.png']

['rotate180.png',
 'rotete6_expanded.png',
 'rotete6.png',
 'rotate90.png',
 'rotate270.png',
 'pasted.png',
 'horizontal_flip.png',
 'svelte.png',
 'vertical_flip.png']

[(1412931,
  '/Users/moqi/Documents/Code/dive-into-python3-practice/resource/output/rotate180.png'),
 (96974,
  '/Users/moqi/Documents/Code/dive-into-python3-practice/resource/output/cropped.png'),
 (1452899,
  '/Users/moqi/Documents/Code/dive-into-python3-practice/resource/output/rotete6_expanded.png'),
 (372825,
  '/Users/moqi/Documents/Code/dive-into-python3-practice/resource/output/quartersized.png'),
 (1373399,
  '/Users/moqi/Documents/Code/dive-into-python3-practice/resource/output/rotete6.png'),
 (1102743,
  '/Users/moqi/Documents/Code/dive-into-python3-practice/resource/output/rotate90.png'),
 (323,
  '/Users/moqi/Documents/Code/dive-into-python3-practice/resource/output/putPixel.png'),
 (16726,
  '/Users/moqi/Documents/Code/dive-into-python3-practice/resource/output/catlogo.png'),
 (1103232,
  '/Users/moqi/Documents/Code/dive-into-python3-practice/resource/output/rotate270.png'),
 (78,
  '/Users/moqi/Documents/Code/dive-into-python3-practice/resource/output/transparentImage.png'),
 (1438798,
  '/Users/moqi/Documents/Code/dive-into-python3-practice/resource/output/pasted.png'),
 (499007,
  '/Users/moqi/Documents/Code/dive-into-python3-practice/resource/output/tiled.png'),
 (538,
  '/Users/moqi/Documents/Code/dive-into-python3-practice/resource/output/purpleImage.png'),
 (1411197,
  '/Users/moqi/Documents/Code/dive-into-python3-practice/resource/output/horizontal_flip.png'),
 (1675874,
  '/Users/moqi/Documents/Code/dive-into-python3-practice/resource/output/svelte.png'),
 (1412210,
  '/Users/moqi/Documents/Code/dive-into-python3-practice/resource/output/vertical_flip.png')]

[('1.3 MiB', 'rotate180.png'),
 ('94.7 KiB', 'cropped.png'),
 ('1.4 MiB', 'rotete6_expanded.png'),
 ('364.1 KiB', 'quartersized.png'),
 ('1.3 MiB', 'rotete6.png'),
 ('1.1 MiB', 'rotate90.png'),
 ('0.3 KiB', 'putPixel.png'),
 ('16.3 KiB', 'catlogo.png'),
 ('1.1 MiB', 'rotate270.png'),
 ('0.1 KiB', 'transparentImage.png'),
 ('1.4 MiB', 'pasted.png'),
 ('487.3 KiB', 'tiled.png'),
 ('0.5 KiB', 'purpleImage.png'),
 ('1.3 MiB', 'horizontal_flip.png'),
 ('1.6 MiB', 'svelte.png'),
 ('1.3 MiB', 'vertical_flip.png')]
"""
