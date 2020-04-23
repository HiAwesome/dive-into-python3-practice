"""
如果你需要获得默认编码的信息，则导入locale模块，然后调用locale.getpreferredencoding()。
在我安装了Windows的笔记本上，它的返回值是'cp1252'，但是在我楼上安装了Linux的台式机上边，它返回'UTF8'。
你看，即使在我自己家里我都不能保证一致性(consistency)！
你的运行结果也许不一样（即使在Windows平台上），这依赖于操作系统的版本和区域/语言选项的设置。
这就是为什么每次打开一个文件的时候指定编码方式是如此重要了。
"""
import locale

print(locale.getpreferredencoding())

"""
UTF-8
"""
