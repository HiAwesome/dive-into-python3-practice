from is_it_true import is_it_true as t

print(type(None))
print(None == False)
print(None == 0)
print(None == '')
print(None is None)

x = None
print(x == None)
y = None
print(x == y)

"""
<class 'NoneType'>
False
False
False
True
True
True
"""

t(None)
t(not None)

"""
no, it is false
yes, it is true
"""
