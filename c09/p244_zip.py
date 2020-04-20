from pprint import pprint

characters = {'S', 'M', 'E', 'D', 'O', 'N', 'R', 'Y'}
guess = {'1', '2', '0', '3', '4', '5', '6', '7'}

pprint(tuple(zip(characters, guess)))
print()

print(dict(zip(characters, guess)))
print()

"""
(('O', '4'),
 ('N', '1'),
 ('R', '2'),
 ('M', '6'),
 ('Y', '5'),
 ('D', '3'),
 ('S', '7'),
 ('E', '0'))

{'O': '4', 'N': '1', 'R': '2', 'M': '6', 'Y': '5', 'D': '3', 'S': '7', 'E': '0'}
"""

