import os

print(os.getcwd())
os.chdir('/Users/moqi/Downloads/output')
print(os.getcwd())

print()
print(os.path.join('/Users/moqi/Documents/Code/dive-into-python3-practice/c04/', 'p108_os1.py'))
print(os.path.join('/Users/moqi/Documents/Code/dive-into-python3-practice/c04', 'p108_os1.py'))

print()
print(os.path.expanduser('~'))
print(os.path.join(os.path.expanduser('~'), 'Documents', 'Code', 'dive-into-python3-practice', 'c04', 'p108_os1.py'))

print()
pathname = '/Users/moqi/Documents/Code/dive-into-python3-practice/c04/p108_os1.py'
print(os.path.split(pathname))
(dirname, filename) = os.path.split(pathname)
print(dirname)
print(filename)
(shortname, extension) = os.path.splitext(filename)
print(shortname)
print(extension)


"""
/Users/moqi/Documents/Code/dive-into-python3-practice/c04
/Users/moqi/Downloads/output

/Users/moqi/Documents/Code/dive-into-python3-practice/c04/p108_os1.py
/Users/moqi/Documents/Code/dive-into-python3-practice/c04/p108_os1.py

/Users/moqi
/Users/moqi/Documents/Code/dive-into-python3-practice/c04/p108_os1.py

('/Users/moqi/Documents/Code/dive-into-python3-practice/c04', 'p108_os1.py')
/Users/moqi/Documents/Code/dive-into-python3-practice/c04
p108_os1.py
p108_os1
.py
"""
