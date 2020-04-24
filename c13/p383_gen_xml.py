import xml.etree.ElementTree as etree

new_feed = etree.Element('{http://www.w3.org/2005/Atom}feed',
                         attrib={'{http://www.w3.org/2005/Atom}lang': 'en'})
print(etree.tostring(new_feed))

"""
b'<ns0:feed xmlns:ns0="http://www.w3.org/2005/Atom" ns0:lang="en" />'
"""
