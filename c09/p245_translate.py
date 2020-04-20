translation_table = {ord('A'): ord('O')}
print(translation_table)
print()

print('MARK'.translate(translation_table))
print()

characters = tuple(ord(c) for c in 'SMEDONRY')
print(characters)
print()

guess = tuple(ord(c) for c in '91570682')
print(guess)
print()

translation_table = dict(zip(characters, guess))
print(translation_table)
print()

print('SEND + MORE == MONEY'.translate(translation_table))
print()

"""
{65: 79}

MORK

(83, 77, 69, 68, 79, 78, 82, 89)

(57, 49, 53, 55, 48, 54, 56, 50)

{83: 57, 77: 49, 69: 53, 68: 55, 79: 48, 78: 54, 82: 56, 89: 50}

9567 + 1085 == 10652
"""
