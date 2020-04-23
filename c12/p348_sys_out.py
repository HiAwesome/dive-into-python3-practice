import sys

for i in range(3):
    print('PapayaWhip')
print()

for i in range(3):
    sys.stdout.write('is the ')
print()

for i in range(3):
    # 目前是棕色🏾
    sys.stderr.write('new black ')
print()

try:
    sys.stdout.read()
except IOError as err:
    print(err)

"""
PapayaWhip
PapayaWhip
PapayaWhip

is the is the is the 

new black new black new black 

not readable
"""
