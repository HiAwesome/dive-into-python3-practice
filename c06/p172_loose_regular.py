import re

pattern = """
    ^                           # beginning of string
    M{0,3}                      # thousands - 0 to 3 Ms
    (CM|CD|D?C{0,3})            # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                                # or 500-800 (D, followed by 0 to 3 Cs)
    (XC|XL|L?X{0,3})            # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                                # or 50-80 (L, followed by 0 to 3 Xs)
    (IX|IV|V?I{0,3})            # ones - 9 (IX), 4 (IV). 0-3 (0 to 3 Is),
                                # or 5-8 (V, followed by 0 to 3 Is)
    $                           # end of string
"""

print(re.search(pattern, 'M', re.VERBOSE))
print(re.search(pattern, 'MCMLXXXIX', re.VERBOSE))
print(re.search(pattern, 'MMMDCCCLXXXVIII', re.VERBOSE))
print(re.search(pattern, 'M'))

"""
/usr/local/bin/python3 /Users/moqi/Documents/Code/dive-into-python3-practice/c06/p172_loose_regular.py
<re.Match object; span=(0, 1), match='M'>
<re.Match object; span=(0, 9), match='MCMLXXXIX'>
<re.Match object; span=(0, 15), match='MMMDCCCLXXXVIII'>
None

Process finished with exit code 0
"""
