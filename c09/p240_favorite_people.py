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

"""
['Dora\n', 'Ethan\n', 'Wesley\n', 'John\n', 'Anne\n', 'Mike\n', 'Chris\n', 'Sarah\n', 'Alex\n', 'Lizzie\n']

['Dora', 'Ethan', 'Wesley', 'John', 'Anne', 'Mike', 'Chris', 'Sarah', 'Alex', 'Lizzie']

['Alex', 'Anne', 'Chris', 'Dora', 'Ethan', 'John', 'Lizzie', 'Mike', 'Sarah', 'Wesley']

['Alex', 'Anne', 'Dora', 'John', 'Mike', 'Chris', 'Ethan', 'Sarah', 'Lizzie', 'Wesley']
"""
