path = '../resource/txt/chinese.txt'

a_file = open(path, encoding='utf-8')

print(a_file.name)
print(a_file.encoding)
print(a_file.mode)
print(a_file.readlines())
print()

a_file = open(path, encoding='utf-8')
print(a_file.read())
# 第二行已经没有数据了，所以是空行
print(a_file.read())
# seek 方法定位到文件中的特定字节
print(a_file.seek(0))
# read 方法可以使用一个可选的参数，即所要读取的字符个数
print(a_file.read(16))
print(a_file.read(1))
print(a_file.read(1))
print(a_file.tell())
print()

print(a_file.seek(17))
print(a_file.read(1))
print(a_file.tell())
print()

print(a_file.seek(18))
"""
为什么这里会失败？因为在第18个字节处不存在字符。距离此处最近的字符从第17个字节开始（长度为三个字节）。
试图从一个字符的中间位置读取会导致程序以UnicodeDecodeError错误失败。
"""
print(a_file.read(1))

"""
../resource/txt/chinese.txt
utf-8
r
['Dive Into Python 是为有经验的程序员编写的一本 Python 书。\n']

Dive Into Python 是为有经验的程序员编写的一本 Python 书。


0
Dive Into Python
 
是
20

17
是
20

18
Traceback (most recent call last):
  File "/Users/moqi/Code/dive-into-python3-practice/c12/p328_open1.py", line 30, in <module>
    print(a_file.read(1))
  File "/usr/local/Cellar/python/3.7.7/Frameworks/Python.framework/Versions/3.7/lib/python3.7/codecs.py", line 322, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0x98 in position 0: invalid start byte
"""
