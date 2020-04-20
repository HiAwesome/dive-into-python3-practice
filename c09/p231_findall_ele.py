import re

print(re.findall('[0-9]+', '16 2-by-4s in rows of 8'))
print(re.findall('[A-Z]+', 'SEND + MORE == MONEY'))
print()

print(re.findall(' s.*? s', "The sixth sick sheikh's sixth sheep's sick."))

"""
['16', '2', '4', '8']
['SEND', 'MORE', 'MONEY']

[' sixth s', " sheikh's s", " sheep's s"]
"""
