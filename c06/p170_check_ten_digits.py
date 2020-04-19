import re

pattern = '^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)$'

print(re.search(pattern, 'MCMXL'))
print(re.search(pattern, 'MCML'))
print(re.search(pattern, 'MCMLX'))
print(re.search(pattern, 'MCMLXXX'))
print(re.search(pattern, 'MCMLXXXX'))

"""
/usr/local/bin/python3 /Users/moqi/Documents/Code/dive-into-python3-practice/c06/p170_check_ten_digits.py
<re.Match object; span=(0, 5), match='MCMXL'>
<re.Match object; span=(0, 4), match='MCML'>
<re.Match object; span=(0, 5), match='MCMLX'>
<re.Match object; span=(0, 7), match='MCMLXXX'>
None

Process finished with exit code 0
"""
