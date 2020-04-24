import xml.etree.ElementTree as etree

from file_path_collect import feed_xml_path as path

tree = etree.parse(path)
root = tree.getroot()
print(root)
print()

print(root.tag)
print(len(root))
for child in root:
    print(child)
print()

print(root.attrib)
print(root[4])
print(root[4].attrib)
print(root[3])
print(root[3].attrib)
print()

"""
<Element '{http://www.w3.org/2005/Atom}feed' at 0x1097b99b0>

{http://www.w3.org/2005/Atom}feed
8
<Element '{http://www.w3.org/2005/Atom}title' at 0x10483a530>
<Element '{http://www.w3.org/2005/Atom}subtitle' at 0x10483a5f0>
<Element '{http://www.w3.org/2005/Atom}id' at 0x10483a650>
<Element '{http://www.w3.org/2005/Atom}updated' at 0x10483a770>
<Element '{http://www.w3.org/2005/Atom}link' at 0x10483a830>
<Element '{http://www.w3.org/2005/Atom}entry' at 0x10483a8f0>
<Element '{http://www.w3.org/2005/Atom}entry' at 0x10483d230>
<Element '{http://www.w3.org/2005/Atom}entry' at 0x10483d6b0>

{'{http://www.w3.org/XML/1998/namespace}lang': 'en'}
<Element '{http://www.w3.org/2005/Atom}link' at 0x10a57c890>
{'rel': 'alternate', 'type': 'text/html', 'href': 'http://diveintomark.org/'}
<Element '{http://www.w3.org/2005/Atom}updated' at 0x10a57c7d0>
{}
"""
