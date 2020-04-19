import re

pattern = '^M{0,3}$'
print(re.search(pattern, 'M'))
print(re.search(pattern, 'MM'))
print(re.search(pattern, 'MMM'))
print(re.search(pattern, 'MMMM'))

"""
/usr/local/bin/python3 /Users/moqi/Documents/Code/dive-into-python3-practice/c06/p166_use_square_bracket.py
<re.Match object; span=(0, 1), match='M'>
<re.Match object; span=(0, 2), match='MM'>
<re.Match object; span=(0, 3), match='MMM'>
None

Process finished with exit code 0
"""
