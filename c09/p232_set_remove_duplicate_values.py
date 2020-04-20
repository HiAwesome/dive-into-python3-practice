a_list = ['The', 'sixth', 'sick', "sheik's", 'sixth', "sheep's", 'sick']
print(a_list)
print(set(a_list))
print()

a_string = 'EAST IS EAST'
print(a_string)
print(set(a_string))
print()

words = ['SEND', 'MORE', 'MONEY']
print(''.join(words))
print(set(''.join(words)))

"""
['The', 'sixth', 'sick', "sheik's", 'sixth', "sheep's", 'sick']
{"sheik's", "sheep's", 'sixth', 'sick', 'The'}

EAST IS EAST
{'T', ' ', 'I', 'A', 'S', 'E'}

SENDMOREMONEY
{'Y', 'O', 'N', 'R', 'S', 'D', 'M', 'E'}
"""
