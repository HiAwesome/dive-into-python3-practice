from pprint import pprint

try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree

from file_path_collect import feed_xml_path as path

tree = etree.parse(path)
root = tree.getroot()
pprint(root.findall('{http://www.w3.org/2005/Atom}entry'))

"""
[<Element {http://www.w3.org/2005/Atom}entry at 0x10203d3c0>,
 <Element {http://www.w3.org/2005/Atom}entry at 0x10203d370>,
 <Element {http://www.w3.org/2005/Atom}entry at 0x10203d230>]
"""
