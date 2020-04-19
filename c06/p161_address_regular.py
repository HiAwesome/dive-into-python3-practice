import re

s = '100 NORTH MAIN ROAD'

print(s.replace('ROAD', 'RD.'))

s = '100 NORTH BROAD ROAD'

print(s.replace('ROAD', 'RD.'))
print(s[:-4] + s[-4:].replace('ROAD', 'RD.'))

print(re.sub('ROAD$', 'RD.', s))

"""
100 NORTH MAIN RD.
100 NORTH BRD. RD.
100 NORTH BROAD RD.
100 NORTH BROAD RD.
"""
