import fractions

from is_it_true import is_it_true

is_it_true(1)
is_it_true(-1)
is_it_true(0)
is_it_true(0.1)
is_it_true(0.0)
is_it_true(fractions.Fraction(1, 2))
is_it_true(fractions.Fraction(0, 1))

"""
yes, it is true
yes, it is true
no, it is false
yes, it is true
no, it is false
yes, it is true
no, it is false
"""
