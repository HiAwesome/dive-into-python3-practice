import re

s = '100 NORTH MAIN ROAD'

print(s.replace('ROAD', 'RD.'))

s = '100 NORTH BROAD ROAD'

print(s.replace('ROAD', 'RD.'))
print(s[:-4] + s[-4:].replace('ROAD', 'RD.'))

print(re.sub('ROAD$', 'RD.', s))

print()
s = '100 BROAD'
print(re.sub('ROAD$', 'RD.', s))
print(re.sub('\\bROAD$', 'RD.', s))
print(re.sub('\bROAD$', 'RD.', s))

print()
s = '100 BROAD ROAD APT. 3'
print(re.sub(r'\bROAD$', 'RD.', s))
print(re.sub(r'\bROAD\b', 'RD.', s))

"""
100 NORTH MAIN RD.
100 NORTH BRD. RD.
100 NORTH BROAD RD.
100 NORTH BROAD RD.

100 BRD.
100 BROAD
100 BROAD

100 BROAD ROAD APT. 3
100 BROAD RD. APT. 3
"""
