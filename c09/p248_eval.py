# eval 调用需要先 import，否则报错
import math
import subprocess

print(eval('1 + 1 == 2'))
print(eval('1 + 1 == 3'))
print(eval('9567 + 1085 == 10652'))
print()

print(eval('"A" + "B"'))
print(eval('"MARK".translate({65: 79})'))
print(eval('"AAAAA".count("A")'))
print(eval('["*"] * 5'))
print()

x = 5
print(eval("x * 5"))
print(eval("pow(x, 2)"))
print(eval("math.sqrt(x)"))
print()

print(eval("subprocess.getoutput('ls ~')"))
print()

# /some/random/file 不要写真实存在路径，为演示的话可以建立单个文件进行删除测试
print(eval("subprocess.getoutput('rm /some/random/file')"))
print()

"""
更坏的是，由于存在全局函数__import__()，它接收字符串形式的模块名，导入模块，并返回模块的引用。
和eval()的能力结合起来，你可以构造一个单独的表达式来删除你所有的文件:
现在想象一下'rm‐rf~'的输出。实际上它不会有任何输出，但是你也不会有任何文件还留着。
"""
print(eval("__import__('subprocess').getoutput('rm /some/random/file')"))

"""
True
False
True

AB
MORK
5
['*', '*', '*', '*', '*']

25
25
2.23606797749979

下面 ... 表示文件夹名或者文件名

...
...
...

...
...


"""
