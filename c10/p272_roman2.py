class OutOfRangeErrer(ValueError):
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
    if n > 3999:
        raise OutOfRangeErrer('number out of range (must be less than 4000)')

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
