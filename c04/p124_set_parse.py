a_set = set(range(10))

print(a_set)
print({x ** 2 for x in a_set})
print({x for x in a_set if x % 2 == 0})
print({2 ** x for x in range(20)})

"""
/usr/local/bin/python3 /Users/moqi/Documents/Code/dive-into-python3-practice/c04/p124_set_parse.py
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
{0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
{0, 2, 4, 6, 8}
{128, 1, 2, 256, 4, 512, 1024, 2048, 8, 4096, 32768, 131072, 262144, 524288, 8192, 16, 16384, 32, 64, 65536}

Process finished with exit code 0

"""
