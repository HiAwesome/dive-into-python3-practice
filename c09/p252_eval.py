x = 5

try:
    eval("x * 5", {}, {})
except NameError as err:
    print(err)
print()

# 你可以通过一个个列出的方式选择性在全局名字空间里面包含一些值。这些——并且这有这些——变量在求值的时候可用。
print(eval("x * 5", {"x": x}, {}))
print()

try:
    # 即使你刚刚导入了 math 模块, 你没有在传给eval()函数的名字空间里包含它，所以求值失败了。
    print(eval("math.sqrt(x)", {"x": x}, {}))
except NameError as err:
    print(err)

"""
name 'x' is not defined

25

name 'math' is not defined
"""
