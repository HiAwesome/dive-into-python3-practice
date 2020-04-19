import sys

from c02.p044_humansize import SUFFIXES

username = 'mark'
password = 'PapayaWhip'

print("{0}'s password is {1}".format(username, password))
print()

# 解析键名的规则非常简单。如果名字以数字开头，则它被当作数字使用，其他情况则被认为是字符串。
si_suffixes = SUFFIXES[1000]
print(si_suffixes)
print('1000{0[0]} = 1{0[1]}'.format(si_suffixes))
print()

print('1MB = 1000{0.modules[c02.p044_humansize].SUFFIXES[1000][0]}'.format(sys))
print()

print('{0:.5f} {1}'.format(697.3456789, 'GB'))

"""
mark's password is PapayaWhip

['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
1000KB = 1MB

1MB = 1000KB

697.34568 GB
"""
