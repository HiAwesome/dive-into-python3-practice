from pprint import pprint

import lxml.etree

from file_path_collect import feed_xml_path as path

tree = lxml.etree.parse(path)
NSMAP = {'atom': 'http://www.w3.org/2005/Atom'}

entries = tree.xpath("//atom:category[@term='accessibility']/..", namespaces=NSMAP)
print(entries)
entry = entries[0]
print(entry.xpath('./atom:title/text()', namespaces=NSMAP))

"""
[<Element {http://www.w3.org/2005/Atom}entry at 0x1089484b0>]
['Accessibility is a harsh mistress']
"""
