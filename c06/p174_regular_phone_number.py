import re

phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
print(phonePattern.search('800-555-1212').groups())
print(phonePattern.search('800-555-1212-1234'))

try:
    print(phonePattern.search('800-555-1212-1234').groups())
except AttributeError as err:
    print(err)

print()
phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})-(\d+)$')
print(phonePattern.search('800-555-1212-1234'))
print(phonePattern.search('800 555 1212 1234'))
print(phonePattern.search('800-555-1212'))

print()
phonePattern = re.compile(r'^(\d{3})\D+(\d{3})\D+(\d{4})\D+(\d+)$')
print(phonePattern.search('800 555 1212 1234').groups())
print(phonePattern.search('800-555-1212-1234').groups())
print(phonePattern.search('80055512121234'))
print(phonePattern.search('800-555-1212'))

print()
phonePattern = re.compile(r'^(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
print(phonePattern.search('80055512121234').groups())
print(phonePattern.search('800.555.1212 x1234').groups())
print(phonePattern.search('800-555-1212').groups())
print(phonePattern.search('(800)5551212 x1234'))

print()
phonePattern = re.compile(r'^\D*(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
print(phonePattern.search('(800)5551212 ext.1234').groups())
print(phonePattern.search('800-555-1212').groups())
print(phonePattern.search('work 1-(800) 555.1212 #1234'))

print()
phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
print(phonePattern.search('work 1-(800) 555.1212 #1234').groups())
print(phonePattern.search('800-555-1212'))
print(phonePattern.search('80055512121234'))

print()
phonePattern = re.compile(r'''
                    # don't match beginning of string, number can start anywhere
    (\d{3})         # area code is 3 digits (e.g. '800')
    \D*             # optional separator is any number of non-digits
    (\d{3})         # trunk is 3 digits (e.g. '555')
    \D*             # optional separator
    (\d{4})         # rest of number is 4 digits (e.g. '1212')
    \D*             # optional separator
    (\d*)           # extension is optional and can be any number of digits
    $               # end of string
''', re.VERBOSE)
print(phonePattern.search('work 1-(800) 555.1212 #1234').groups())
print(phonePattern.search('800-555-1212'))

"""
('800', '555', '1212')
None
'NoneType' object has no attribute 'groups'

<re.Match object; span=(0, 17), match='800-555-1212-1234'>
None
None

('800', '555', '1212', '1234')
('800', '555', '1212', '1234')
None
None

('800', '555', '1212', '1234')
('800', '555', '1212', '1234')
('800', '555', '1212', '')
None

('800', '555', '1212', '1234')
('800', '555', '1212', '')
None

('800', '555', '1212', '1234')
<re.Match object; span=(0, 12), match='800-555-1212'>
<re.Match object; span=(0, 14), match='80055512121234'>

('800', '555', '1212', '1234')
<re.Match object; span=(0, 12), match='800-555-1212'>
"""
