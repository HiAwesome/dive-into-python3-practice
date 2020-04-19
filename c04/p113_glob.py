import glob
import os
import pprint

os.chdir('/Users/moqi/Downloads/output')
pprint.pprint(glob.glob('withLogo/*.png'))
print()
pprint.pprint(glob.glob('*.png'))

"""
['withLogo/rotate180.png',
 'withLogo/cropped.png',
 'withLogo/rotete6_expanded.png',
 'withLogo/quartersized.png',
 'withLogo/rotete6.png',
 'withLogo/rotate90.png',
 'withLogo/putPixel.png',
 'withLogo/rotate270.png',
 'withLogo/transparentImage.png',
 'withLogo/pasted.png',
 'withLogo/tiled.png',
 'withLogo/purpleImage.png',
 'withLogo/horizontal_flip.png',
 'withLogo/svelte.png',
 'withLogo/vertical_flip.png']

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
"""
