assert 1 + 1 == 2

try:
    assert 1 + 1 == 3
except AssertionError as err:
    print(err.__class__)

try:
    assert 2 + 2 == 5, 'Only for very large values of 2'
except AssertionError as err:
    print(err)

"""
<class 'AssertionError'>
Only for very large values of 2
"""
