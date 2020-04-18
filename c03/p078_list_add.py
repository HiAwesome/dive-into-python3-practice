a_list = ['a']

a_list = a_list + [2.0, 3]
print(a_list)

a_list.append(True)
print(a_list)

a_list.extend(['four', '&'])
print(a_list)

a_list.insert(0, '****')
print(a_list)

"""
/usr/local/bin/python3 /Users/moqi/Documents/Code/dive-into-python3-practice/c03/p078_list_add.py
['a', 2.0, 3]
['a', 2.0, 3, True]
['a', 2.0, 3, True, 'four', '&']
['****', 'a', 2.0, 3, True, 'four', '&']

Process finished with exit code 0
"""

b_list = ['a', 'b', 'c']
b_list.extend(['d', 'e', 'f'])
print(b_list)
print(len(b_list))
print(b_list[-1])

b_list.append(['g', 'h', 'i'])
print(b_list)
print(len(b_list))
print(b_list[-1])

"""
['a', 'b', 'c', 'd', 'e', 'f']
6
f
['a', 'b', 'c', 'd', 'e', 'f', ['g', 'h', 'i']]
7
['g', 'h', 'i']
"""
