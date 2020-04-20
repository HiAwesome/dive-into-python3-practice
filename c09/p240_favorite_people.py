names = list(open('../resource/txt/favorite-people.txt', encoding='utf-8'))
print(names)
print()

names = [name.rstrip() for name in names]
print(names)
print()

names = sorted(names)
print(names)
print()

names = sorted(names, key=len)
print(names)
print()

"""
['Dora\n', 'Ethan\n', 'Wesley\n', 'John\n', 'Anne\n', 'Mike\n', 'Chris\n', 'Sarah\n', 'Alex\n', 'Lizzie\n']

['Dora', 'Ethan', 'Wesley', 'John', 'Anne', 'Mike', 'Chris', 'Sarah', 'Alex', 'Lizzie']

['Alex', 'Anne', 'Chris', 'Dora', 'Ethan', 'John', 'Lizzie', 'Mike', 'Sarah', 'Wesley']

['Alex', 'Anne', 'Dora', 'John', 'Mike', 'Chris', 'Ethan', 'Sarah', 'Lizzie', 'Wesley']
"""
