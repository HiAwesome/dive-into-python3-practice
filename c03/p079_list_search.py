a_list = ['a', 'b', 'new', 'mpilgrim', 'new']

print(a_list.count('new'))
print('new' in a_list)
print('c' in a_list)
print(a_list.index('mpilgrim'))
print(a_list.index('new'))
print(a_list.index('c'))

"""
2
True
False
3
2
Traceback (most recent call last):
  File "/Users/moqi/Documents/Code/dive-into-python3-practice/c03/p079_list_search.py", line 8, in <module>
    print(a_list.index('c'))
ValueError: 'c' is not in list
"""
