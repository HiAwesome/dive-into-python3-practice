from is_it_true import is_it_true

is_it_true(())
is_it_true(('a', 'b'))
is_it_true((False,))

print(type(False))
print(type((False,)))

"""
no, it is false
yes, it is true
yes, it is true
<class 'bool'>
<class 'tuple'>
"""
