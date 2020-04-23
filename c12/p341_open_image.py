from file_path_collect import beauregard_path

an_image = open(beauregard_path, mode='rb')

print(an_image.mode)
print(an_image.name)

try:
    print(an_image.encoding)
except AttributeError as err:
    print(err)

"""
rb
../resource/image/beauregard.jpg
'_io.BufferedReader' object has no attribute 'encoding'
"""
