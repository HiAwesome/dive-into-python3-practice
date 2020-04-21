print(eval("pow(5, 2)", {}, {}))
print(eval("__import__('math').sqrt(5)", {}, {}))
print()

print(eval("__import__('subprocess').getoutput('rm /some/random/file')", {}, {}))
print()

try:
    print(eval("__import__('math').sqrt(25)", {"__builtins__": None}, {}))
except TypeError as err:
    print(err)
print()

try:
    print(eval("__import__('subprocess').getoutput('rm /some/random/file')", {"__builtins__": None}, {}))
except TypeError as err:
    print(err)
print()

print(eval("2 ** 222", {"__builtins__": None}, {}))

"""
25
2.23606797749979

rm: /some/random/file: No such file or directory

'NoneType' object is not subscriptable

'NoneType' object is not subscriptable

6739986666787659948666753771754907668409286105635143120275902562304
"""
