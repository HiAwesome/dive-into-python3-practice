"""
1. discard()接受一个单值作为参数，并从集合中删除该值。
2. 如果针对一个集合中不存在的值调用discard()方法，它不进行任何操作。不产生错误；只是一条空指令。
3. remove()方法也接受一个单值作为参数，也从集合中将其删除。
4. 区别在这里：如果该值不在集合中，remove()方法引发一个KeyError例外。
"""
a_set = {1, 3, 6, 10, 15, 21, 44, 56}
print(a_set)

a_set.discard(10)
print(a_set)

a_set.discard(10)
print(a_set)

a_set.remove(21)
print(a_set)

try:
    a_set.remove(21)
except KeyError as err:
    print('the key %s is not exist now.' % err)

print()
print(a_set.pop())
print(a_set.pop())
print(a_set.pop())
print(a_set.pop())
print(a_set.pop())
print(a_set)

a_set.clear()
print(a_set)

"""
{1, 3, 6, 10, 44, 15, 21, 56}
{1, 3, 6, 44, 15, 21, 56}
{1, 3, 6, 44, 15, 21, 56}
{1, 3, 6, 44, 15, 56}
the key 21 is not exist now.

1
3
6
44
15
{56}
set()
"""
