import re

old_pattern = '^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$'
pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

print(re.search(pattern, 'MDLV'))
print(re.search(pattern, 'MMDCLXVI'))
print(re.search(pattern, 'MMMDCCCLXXXVIII'))
print(re.search(pattern, 'I'))

"""
/usr/local/bin/python3 /Users/moqi/Documents/Code/dive-into-python3-practice/c06/p171_check_digits.py
<re.Match object; span=(0, 4), match='MDLV'>
<re.Match object; span=(0, 8), match='MMDCLXVI'>
<re.Match object; span=(0, 15), match='MMMDCCCLXXXVIII'>
<re.Match object; span=(0, 1), match='I'>

Process finished with exit code 0
"""
