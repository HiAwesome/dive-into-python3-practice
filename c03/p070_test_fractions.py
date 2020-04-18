import fractions

x = fractions.Fraction(1, 3)

print(x)
print(x * 2)
print(fractions.Fraction(100, 50))
print(fractions.Fraction(100, 0))

"""
/usr/local/bin/python3 /Users/moqi/Documents/Code/dive-into-python3-practice/c03/p070_test_fractions.py
1/3
2/3
2
Traceback (most recent call last):
  File "/Users/moqi/Documents/Code/dive-into-python3-practice/c03/p070_test_fractions.py", line 8, in <module>
    print(fractions.Fraction(100, 0))
  File "/usr/local/Cellar/python/3.7.7/Frameworks/Python.framework/Versions/3.7/lib/python3.7/fractions.py", line 178, in __new__
    raise ZeroDivisionError('Fraction(%s, 0)' % numerator)
ZeroDivisionError: Fraction(100, 0)

Process finished with exit code 1

"""
