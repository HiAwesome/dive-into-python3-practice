path = '../resource/txt/chinese.txt'

a_file = open(path, encoding='utf-8')

print(a_file.name)
print(a_file.encoding)
print(a_file.mode)
print(a_file.readlines())

"""
../resource/txt/chinese.txt
utf-8
r
['Dive Into Python 是为有经验的程序员编写的一本 Python 书。\n']
"""
