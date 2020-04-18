import sys, pprint

pprint.pprint(sys.path)
print()
pprint.pprint(sys)

'''
1. 通过添加一个目录名称到sys.path里，你可以在运行时添加一个新的目录到Python的搜索路径中，
   然后无论任何时候你想导入一个模块，Python都会同样的去查找那个目录。只要Python在运行，都会一直有效。
2. 通过使用sys.path.insert(0,new_path)，你可以插入一个新的目录到sys.path列表的第一项，从而使其出现在Python搜索路径的开头。
   这几乎总是你想要的。万一出现名字冲突（例如，Python自带了版本2的一个特定的库，但是你想使用版本3），
   这个方法就能确保你的模块能够被发现和使用，替代Python自带的版本。
'''
sys.path.insert(0, '/Users/moqi/Documents/Code/automate-the-boring-stuff')
print()
pprint.pprint(sys.path)

"""
['/Users/moqi/Documents/Code/dive-into-python3-practice/c01',
 '/Users/moqi/Documents/Code/dive-into-python3-practice',
 '/Users/moqi/Library/Application '
 'Support/JetBrains/Toolbox/apps/PyCharm-P/ch-0/201.6668.28/PyCharm 2020.1 '
 'EAP.app/Contents/plugins/python/helpers/pycharm_display',
 '/usr/local/Cellar/python/3.7.7/Frameworks/Python.framework/Versions/3.7/lib/python37.zip',
 '/usr/local/Cellar/python/3.7.7/Frameworks/Python.framework/Versions/3.7/lib/python3.7',
 '/usr/local/Cellar/python/3.7.7/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload',
 '/Users/moqi/Library/Python/3.7/lib/python/site-packages',
 '/usr/local/lib/python3.7/site-packages',
 '/Users/moqi/Library/Application '
 'Support/JetBrains/Toolbox/apps/PyCharm-P/ch-0/201.6668.28/PyCharm 2020.1 '
 'EAP.app/Contents/plugins/python/helpers/pycharm_matplotlib_backend']

<module 'sys' (built-in)>

['/Users/moqi/Documents/Code/automate-the-boring-stuff',
 '/Users/moqi/Documents/Code/dive-into-python3-practice/c01',
 '/Users/moqi/Documents/Code/dive-into-python3-practice',
 '/Users/moqi/Library/Application '
 'Support/JetBrains/Toolbox/apps/PyCharm-P/ch-0/201.6668.28/PyCharm 2020.1 '
 'EAP.app/Contents/plugins/python/helpers/pycharm_display',
 '/usr/local/Cellar/python/3.7.7/Frameworks/Python.framework/Versions/3.7/lib/python37.zip',
 '/usr/local/Cellar/python/3.7.7/Frameworks/Python.framework/Versions/3.7/lib/python3.7',
 '/usr/local/Cellar/python/3.7.7/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload',
 '/Users/moqi/Library/Python/3.7/lib/python/site-packages',
 '/usr/local/lib/python3.7/site-packages',
 '/Users/moqi/Library/Application '
 'Support/JetBrains/Toolbox/apps/PyCharm-P/ch-0/201.6668.28/PyCharm 2020.1 '
 'EAP.app/Contents/plugins/python/helpers/pycharm_matplotlib_backend']
 
"""
