from pprint import pprint

import lxml.etree

from file_path_collect import feed_xml_path as path

tree = lxml.etree.parse(path)
pprint(tree.findall('//{http://www.w3.org/2005/Atom}*[@href]'))
print()

pprint(tree.findall("//{http://www.w3.org/2005/Atom}*[@href='http://diveintomark.org/']"))
print()

NS = '{http://www.w3.org/2005/Atom}'
pprint(tree.findall('//{NS}author[{NS}uri]'.format(NS=NS)))

"""
[<Element {http://www.w3.org/2005/Atom}link at 0x108df61e0>,
 <Element {http://www.w3.org/2005/Atom}link at 0x108dec960>,
 <Element {http://www.w3.org/2005/Atom}link at 0x108dec9b0>,
 <Element {http://www.w3.org/2005/Atom}link at 0x108df6230>]
 
[<Element {http://www.w3.org/2005/Atom}link at 0x10349f7d0>]
 
[<Element {http://www.w3.org/2005/Atom}author at 0x10ae79730>,
 <Element {http://www.w3.org/2005/Atom}author at 0x10ae796e0>]
"""
