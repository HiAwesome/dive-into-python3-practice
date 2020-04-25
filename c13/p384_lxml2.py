import lxml.etree

NSMAP = {None: 'http://www.w3.org/2005/Atom'}
new_feed = lxml.etree.Element('feed', nsmap=NSMAP)
print(lxml.etree.tounicode(new_feed))
print()

new_feed.set('{http://www.w3.org/XML/1998/namespace}lang', 'en')
print(lxml.etree.tounicode(new_feed))
print()

title = lxml.etree.SubElement(new_feed, 'title', attrib={'type': 'html'})
print(lxml.etree.tounicode(new_feed))
print()

title.text = 'dive into & hellip;'
print(lxml.etree.tounicode(new_feed))
print()

print(lxml.etree.tounicode(new_feed, pretty_print=True))

"""
<feed xmlns="http://www.w3.org/2005/Atom"/>

<feed xmlns="http://www.w3.org/2005/Atom" xml:lang="en"/>

<feed xmlns="http://www.w3.org/2005/Atom" xml:lang="en"><title type="html"/></feed>

<feed xmlns="http://www.w3.org/2005/Atom" xml:lang="en"><title type="html">dive into &amp; hellip;</title></feed>

<feed xmlns="http://www.w3.org/2005/Atom" xml:lang="en">
  <title type="html">dive into &amp; hellip;</title>
</feed>
"""
