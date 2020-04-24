import xml.etree.ElementTree as etree
from pprint import pprint

from file_path_collect import feed_xml_path as path

tree = etree.parse(path)
root = tree.getroot()

pprint(root.findall('{http://www.w3.org/2005/Atom}entry'))
print(root.tag)
print(root.findall('{http://www.w3.org/2005/Atom}feed'))
print(root.findall('{http://www.w3.org/2005/Atom}author'))
print()

pprint(tree.findall('{http://www.w3.org/2005/Atom}entry'))
print(tree.findall('{http://www.w3.org/2005/Atom}author'))
print()

"""
[<Element '{http://www.w3.org/2005/Atom}entry' at 0x1016a7590>,
 <Element '{http://www.w3.org/2005/Atom}entry' at 0x1016a7e90>,
 <Element '{http://www.w3.org/2005/Atom}entry' at 0x1016aa350>]
{http://www.w3.org/2005/Atom}feed
[]
[]

[<Element '{http://www.w3.org/2005/Atom}entry' at 0x10f8cf650>,
 <Element '{http://www.w3.org/2005/Atom}entry' at 0x10f8cff50>,
 <Element '{http://www.w3.org/2005/Atom}entry' at 0x10f8d2410>]
[]
"""
