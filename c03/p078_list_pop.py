a_list = ['a', 'b', 'new', 'mpilgrim']

print(a_list.pop())
print(a_list)

print(a_list.pop(1))
print(a_list)

print(a_list.pop())
print(a_list)

print(a_list.pop())
print(a_list)

print(a_list.pop())
print(a_list)

"""
mpilgrim
['a', 'b', 'new']
b
['a', 'new']
new
['a']
a
[]
Traceback (most recent call last):
  File "/Users/moqi/Documents/Code/dive-into-python3-practice/c03/p078_list_pop.py", line 15, in <module>
    print(a_list.pop())
IndexError: pop from empty list
"""
