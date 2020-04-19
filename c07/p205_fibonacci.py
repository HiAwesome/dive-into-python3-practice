def fib(ele):
    a, b = 0, 1
    while a < ele:
        yield a
        a, b = b, a + b


"""
在本目录命令行执行以下代码：
>>> from p205_fibonacci import fib
>>> for n in fib(1000):
...     print(n, end=' ')
... 
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 
>>> list(fib(1000))
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
>>> 
"""
