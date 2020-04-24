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

entries = tree.findall('{http://www.w3.org/2005/Atom}entry')
print(len(entries))
title_element = entries[0].find('{http://www.w3.org/2005/Atom}title')
print(title_element.text)
foo_element = entries[0].find('{http://www.w3.org/2005/Atom}foo')
print(foo_element)
print(type(foo_element))
print()

"""
这里不带最开头的点会出现警告⚠️：
FutureWarning: This search is broken in 1.3 and earlier, and will be fixed in a future version. 
 If you rely on the current behaviour, change it to './/{http://www.w3.org/2005/Atom}link'
  all_links = tree.findall('//{http://www.w3.org/2005/Atom}link')
"""
all_links = tree.findall('.//{http://www.w3.org/2005/Atom}link')
pprint(all_links)
pprint(all_links[0].attrib)
pprint(all_links[1].attrib)
pprint(all_links[2].attrib)
pprint(all_links[3].attrib)

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

3
Dive into history, 2009 edition
None
<class 'NoneType'>

[<Element '{http://www.w3.org/2005/Atom}link' at 0x10e6c2710>,
 <Element '{http://www.w3.org/2005/Atom}link' at 0x10e6c2b90>,
 <Element '{http://www.w3.org/2005/Atom}link' at 0x10e6c7350>,
 <Element '{http://www.w3.org/2005/Atom}link' at 0x10e6c7710>]
{'href': 'http://diveintomark.org/', 'rel': 'alternate', 'type': 'text/html'}
{'href': 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition',
 'rel': 'alternate',
 'type': 'text/html'}
{'href': 'http://diveintomark.org/archives/2009/03/21/accessibility-is-a-harsh-mistress',
 'rel': 'alternate',
 'type': 'text/html'}
{'href': 'http://diveintomark.org/archives/2008/12/18/give-part-1-container-formats',
 'rel': 'alternate',
 'type': 'text/html'}
"""
