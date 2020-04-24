import xml.etree.ElementTree as etree

from file_path_collect import feed_xml_path as path

tree = etree.parse(path)
root = tree.getroot()
print(root)

"""
<Element '{http://www.w3.org/2005/Atom}feed' at 0x1097b99b0>
"""
