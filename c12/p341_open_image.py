from file_path_collect import beauregard_path

an_image = open(beauregard_path, mode='rb')

print(an_image.mode)
print(an_image.name)

try:
    print(an_image.encoding)
except AttributeError as err:
    print(err)
print()

print(an_image.tell())
data = an_image.read(3)
print(data)
print(type(data))
print(an_image.tell())
print(an_image.seek(0))
data = an_image.read()
print(len(data))

"""
rb
../resource/image/beauregard.jpg
'_io.BufferedReader' object has no attribute 'encoding'

0
b'\xff\xd8\xff'
<class 'bytes'>
3
0
3150
"""
