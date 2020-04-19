import re

pattern = '^M?M?M?(CM|CD|D?C?C?C?)$'

print(re.search(pattern, 'MCM'))
print(re.search(pattern, 'MD'))
print(re.search(pattern, 'MMMCCC'))
print(re.search(pattern, 'MCMC'))
print(re.search(pattern, ''))

"""
/usr/local/bin/python3 /Users/moqi/Documents/Code/dive-into-python3-practice/c06/p165_check_hundreds.py
<re.Match object; span=(0, 3), match='MCM'>
<re.Match object; span=(0, 2), match='MD'>
<re.Match object; span=(0, 6), match='MMMCCC'>
None
<re.Match object; span=(0, 0), match=''>

Process finished with exit code 0
"""
