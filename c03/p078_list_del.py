a_list = ['a', 'b', 'new', 'mpilgrim', 'new']

print(a_list)

print(a_list[1])
del a_list[1]
print(a_list)
print(a_list[1])

a_list.remove('new')
print(a_list)

a_list.remove('new')
print(a_list)

a_list.remove('new')
print(a_list)

"""
['a', 'b', 'new', 'mpilgrim', 'new']
b
['a', 'new', 'mpilgrim', 'new']
new
['a', 'mpilgrim', 'new']
['a', 'mpilgrim']
Traceback (most recent call last):
  File "/Users/moqi/Documents/Code/dive-into-python3-practice/c03/p078_list_del.py", line 16, in <module>
    a_list.remove('new')
ValueError: list.remove(x): x not in list
"""
