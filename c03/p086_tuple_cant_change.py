a_tuple = ('a', 'b', 'mpilgrim', 'z', 'example')

try:
    a_tuple.append('new')
except AttributeError as err:
    print(err)

try:
    a_tuple.remove('z')
except AttributeError as err:
    print(err)

print(a_tuple.index('z'))
print('exaple' in a_tuple)

"""
'tuple' object has no attribute 'append'
'tuple' object has no attribute 'remove'
3
False
"""
