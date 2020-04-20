import itertools
import pprint


def next_perms_print(inner_perms):
    print(next(inner_perms))
    print(next(inner_perms))
    print(next(inner_perms))
    print(next(inner_perms))
    print(next(inner_perms))
    print(next(inner_perms))
    try:
        print(next(inner_perms))
    except StopIteration as err:
        print(err.__class__)


perms = itertools.permutations([1, 2, 3], 2)
next_perms_print(perms)
print()

perms = itertools.permutations('abc', 3)
next_perms_print(perms)
print()

pprint.pprint(list(itertools.permutations('ABC', 3)))
print()

# itertools.product()函数返回包含两个序列的笛卡尔乘积的迭代器。
pprint.pprint(list(itertools.product('ABC', '123')))
print()

"""
itertools.combinations()函数返回包含给定序列的给定长度的所有组合的迭代器。这和itertools.permutations()函数很类似，
除了不包含因为只有顺序不同而重复的情况。
所以itertools.permutations('ABC',2)同时返回('A','B')and('B','A')(同其它的排列一起),
itertools.combinations('ABC',2)不会返回('B','A')，因为它和('A','B')是重复的，只是顺序不同而已。
"""
pprint.pprint(list(itertools.combinations('ABC', 2)))
print()

"""
(1, 2)
(1, 3)
(2, 1)
(2, 3)
(3, 1)
(3, 2)
<class 'StopIteration'>

('a', 'b', 'c')
('a', 'c', 'b')
('b', 'a', 'c')
('b', 'c', 'a')
('c', 'a', 'b')
('c', 'b', 'a')
<class 'StopIteration'>

[('A', 'B', 'C'),
 ('A', 'C', 'B'),
 ('B', 'A', 'C'),
 ('B', 'C', 'A'),
 ('C', 'A', 'B'),
 ('C', 'B', 'A')]
 
[('A', '1'),
 ('A', '2'),
 ('A', '3'),
 ('B', '1'),
 ('B', '2'),
 ('B', '3'),
 ('C', '1'),
 ('C', '2'),
 ('C', '3')]
 
[('A', 'B'), ('A', 'C'), ('B', 'C')]

"""
