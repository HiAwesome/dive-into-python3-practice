a_set = {2, 3, 4, 5, 6, 196}
print(a_set)
print(3 in a_set)
print(31 in a_set)
print()

b_set = {4, 5, 6, 900}
print(a_set.union(b_set))
print(a_set.intersection(b_set))
print(a_set.difference(b_set))
print(a_set.symmetric_difference(b_set))
print()

print(b_set.symmetric_difference(a_set))
print(b_set.symmetric_difference(a_set) == a_set.symmetric_difference(b_set))
print(b_set.union(a_set) == a_set.union(b_set))
print(b_set.intersection(a_set) == a_set.intersection(b_set))
print(b_set.difference(a_set) == a_set.difference(b_set))
print()

c_set = {1,2,3}
d_set = {1,2,3,4}
print(c_set.issubset(d_set))
print(d_set.issuperset(c_set))
c_set.add(5)
print(c_set.issubset(d_set))
print(d_set.issuperset(c_set))

"""
{2, 3, 4, 5, 6, 196}
True
False

{2, 3, 4, 5, 6, 196, 900}
{4, 5, 6}
{2, 3, 196}
{2, 3, 900, 196}

{2, 3, 196, 900}
True
True
True
False

True
True
False
False
"""
