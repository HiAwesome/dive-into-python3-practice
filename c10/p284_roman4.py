class OutOfRangeErrer(ValueError):
    """
    事实上，异常类可以不做任何事情，但是至少添加一行代码使其成为一个类。
    pass 的真正意思是什么都不做，但是它是一行 Python 代码，所以可以使其成为类。
    """
    pass


class NotIntegerError(ValueError):
    pass


roman_numeral_map = (('M', 1000),
                     ('CM', 900),
                     ('D', 500),
                     ('CD', 400),
                     ('C', 100),
                     ('XC', 90),
                     ('L', 50),
                     ('XL', 40),
                     ('X', 10),
                     ('IX', 9),
                     ('V', 5),
                     ('IV', 4),
                     ('I', 1))


def to_roman(n):
    """convert integer to Roman numeral"""
    if not isinstance(n, int):
        raise NotIntegerError('non-integers can not be converted')
    if not 0 < n < 4000:
        raise OutOfRangeErrer('number out of range (must be 1..3999)')

    result = ''
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer
            # print('subtracting {0} from input, adding {1} to output'.format(integer, numeral))

    return result


if __name__ == '__main__':
    to_roman(1424)

"""
subtracting 1000 from input, adding M to output
subtracting 400 from input, adding CD to output
subtracting 10 from input, adding X to output
subtracting 10 from input, adding X to output
subtracting 4 from input, adding IV to output
"""
