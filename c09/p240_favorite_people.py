import itertools
from pprint import pprint

names = list(open('../resource/txt/favorite-people.txt', encoding='utf-8'))
print(names)
print()

"""
不幸的是，(对于这个例子来说),list(open(filename))表达式返回的每一行的末尾都包含回车。
这个列表解析使用rstrip()字符串方法移除每一行尾部的空白。
(字符串也有一个lstrip()方法移除头部的空白，以及strip()方法头尾都移除。)
"""
names = [name.rstrip() for name in names]
print(names)
print()

names = sorted(names)
print(names)
print()

names = sorted(names, key=len)
print(names)
print()

groups = itertools.groupby(names, len)
print(groups)
pprint(list(groups))
print()

groups = itertools.groupby(names, len)
for name_length, name_iter in groups:
    print('Names with {0:d} letters'.format(name_length))
    for name in name_iter:
        print(name)
print()

print(list(range(0, 3)))
print(list(range(10, 13)))
print(list(itertools.chain(range(0, 3), range(10, 13))))
print(list(zip(range(0, 3), range(10, 13))))
print(list(zip(range(0, 3), range(10, 14))))
print(list(itertools.zip_longest(range(0, 3), range(10, 14))))
print()

"""
['Dora\n', 'Ethan\n', 'Wesley\n', 'John\n', 'Anne\n', 'Mike\n', 'Chris\n', 'Sarah\n', 'Alex\n', 'Lizzie\n']

['Dora', 'Ethan', 'Wesley', 'John', 'Anne', 'Mike', 'Chris', 'Sarah', 'Alex', 'Lizzie']

['Alex', 'Anne', 'Chris', 'Dora', 'Ethan', 'John', 'Lizzie', 'Mike', 'Sarah', 'Wesley']

['Alex', 'Anne', 'Dora', 'John', 'Mike', 'Chris', 'Ethan', 'Sarah', 'Lizzie', 'Wesley']

<itertools.groupby object at 0x10ee617d0>
[(4, <itertools._grouper object at 0x10e050e10>),
 (5, <itertools._grouper object at 0x10e050e50>),
 (6, <itertools._grouper object at 0x10e050e90>)]

Names with 4 letters
Alex
Anne
Dora
John
Mike
Names with 5 letters
Chris
Ethan
Sarah
Names with 6 letters
Lizzie
Wesley

[0, 1, 2]
[10, 11, 12]
[0, 1, 2, 10, 11, 12]
[(0, 10), (1, 11), (2, 12)]
[(0, 10), (1, 11), (2, 12)]
[(0, 10), (1, 11), (2, 12), (None, 13)]
"""
