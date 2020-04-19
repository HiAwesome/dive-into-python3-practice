by = b'abcd\x65'

print(by)
print(type(by))
print(len(by))
print()

by += b'\xff'
print(by)
print(len(by))
print(by[0])

try:
    by[0] = 100
except TypeError as err:
    print(err)

print()
by = b'abcd\x65'
barr = bytearray(by)
print(barr)
print(len(barr))
barr[0] = 102
print(barr)

print()
by = b'd'
s = 'abcde'
try:
    by + s
except TypeError as err:
    print(err)

try:
    s.count(by)
except TypeError as err:
    print(err)

print(s.count(by.decode('ascii')))

print()
a_string = '深入 Python3'
print(len(a_string))
by = a_string.encode('utf-8')
print(by)
print(len(by))
by2 = a_string.encode('gb18030')
print(by2)
print(len(by2))
by3 = a_string.encode('big5')
print(by3)
print(len(by3))
roundtrip = by3.decode('big5')
print(roundtrip)
print(a_string == roundtrip)

"""
b'abcde'
<class 'bytes'>
5

b'abcde\xff'
6
97
'bytes' object does not support item assignment

bytearray(b'abcde')
5
bytearray(b'fbcde')


can't concat str to bytes
must be str, not bytes
1

10
b'\xe6\xb7\xb1\xe5\x85\xa5 Python3'
14
b'\xc9\xee\xc8\xeb Python3'
12
b'\xb2`\xa4J Python3'
12
深入 Python3
True
"""
