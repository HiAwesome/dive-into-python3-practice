unique_characters = {'E', 'D', 'M', 'O', 'N', 'N', 'R', 'Y'}

gen = (ord(c) for c in unique_characters)

print(gen)
print(next(gen))
print(next(gen))
print(tuple(ord(c) for c in unique_characters))
print()


def ord_map(a_string):
    for c in a_string:
        yield ord(c)


gen2 = ord_map(unique_characters)
print(list(gen2))

"""
<generator object <genexpr> at 0x10e6e9d50>
89
68
(89, 68, 69, 79, 82, 77, 78)

[79, 78, 68, 77, 82, 69, 89]
"""
