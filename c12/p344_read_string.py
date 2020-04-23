import io

a_string = 'PapayaWhip is the new black.'
"""
io.StringIO让你能够将一个字符串作为文本文件来看待。
另外还有一个io.ByteIO类，它允许你将字节数组当作二进制文件来处理
"""
a_file = io.StringIO(a_string)

print(a_file.read())
print(a_file.read())
print(a_file.seek(0))
print(a_file.read(10))
print(a_file.tell())
print(a_file.seek(18))
print(a_file.read())

"""
PapayaWhip is the new black.

0
PapayaWhip
10
18
new black.
"""
