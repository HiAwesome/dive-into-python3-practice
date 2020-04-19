def make_counter(x):
    print('entering make_counter')
    while True:
        yield x
        print('incrementing x')
        x += 1


"""
在本目录命令行执行以下代码：
>>> from p203_make_counter import make_counter
>>> counter = make_counter(2)
>>> counter
<generator object make_counter at 0x10b01ccd0>
>>> next(counter)
entering make_counter
2
>>> next(counter)
incrementing x
3
>>> next(counter)
incrementing x
4
>>> next(counter)
incrementing x
5
"""
