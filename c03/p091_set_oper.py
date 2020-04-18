a_set = {1, 2}
a_set.add(4)

print(a_set)
print(len(a_set))

a_set.add(1)
print(a_set)
print(len(a_set))

"""
{1, 2, 4}
3
{1, 2, 4}
3
"""

b_set = {1, 2, 3}
print(b_set)
b_set.update({2, 4, 6})
print(b_set)
b_set.update({3, 6, 9}, {90, 98, 99})
print(b_set)
b_set.update([10, 20, 30])
print(b_set)

"""
{1, 2, 3}
{1, 2, 3, 4, 6}
{1, 2, 3, 4, 99, 6, 98, 9, 90}
{1, 2, 3, 4, 99, 6, 98, 9, 10, 20, 90, 30}
"""
