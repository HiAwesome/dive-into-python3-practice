import pprint

s = """Finished files are the re-
sult of years of scientif-
ic study combined with the
experience of years.
"""

pprint.pprint(s.splitlines())
print()

pprint.pprint(s.lower())
print()

print(s.lower().count('f'))

"""
['Finished files are the re-',
 'sult of years of scientif-',
 'ic study combined with the',
 'experience of years.']
 
('finished files are the re-\n'
 'sult of years of scientif-\n'
 'ic study combined with the\n'
 'experience of years.\n')
 
6
"""
