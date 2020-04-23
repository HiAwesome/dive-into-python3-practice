class OutOfRangeErrer(ValueError):
    """
    事实上，异常类可以不做任何事情，但是至少添加一行代码使其成为一个类。
    pass 的真正意思是什么都不做，但是它是一行 Python 代码，所以可以使其成为类。
    """
    pass


class NotIntegerError(ValueError):
    pass


class InvalidRomanNumeralError(ValueError):
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

to_roman_table = [None]
from_roman_table = {}


def to_roman(n):
    """convert integer to Roman numeral"""
    if int(n) != n:
        raise NotIntegerError('non-integers can not be converted')
    if not 0 < n < 5000:
        raise OutOfRangeErrer('number out of range (must be 1..4999)')
    return to_roman_table[n]


def from_roman(s):
    """convert Roman numeral to integer"""
    if not isinstance(s, str):
        raise InvalidRomanNumeralError('Input must be a string')
    if not s:
        raise InvalidRomanNumeralError('Input can not be blank')
    if s not in from_roman_table:
        raise InvalidRomanNumeralError('Invalid Roman numeral: {0}'.format(s))
    return from_roman_table[s]


def build_lookup_tables():
    def to_roman(n):
        result = ''
        for numeral, integer in roman_numeral_map:
            if n >= integer:
                result = numeral
                n -= integer
                break
        # 注意这个缩进级别，和 for 循环平行
        if n > 0:
            result += to_roman_table[n]
        return result

    for integer in range(1, 5000):
        roman_numeral = to_roman(integer)
        to_roman_table.append(roman_numeral)
        from_roman_table[roman_numeral] = integer


build_lookup_tables()
