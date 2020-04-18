a_dict = {'server': 'db.div.org', 'db': 'mysql'}
print(a_dict)

print(a_dict['db'])
print(a_dict['server'])

print(a_dict['mysql'])

"""
{'server': 'db.div.org', 'db': 'mysql'}
mysql
db.div.org
Traceback (most recent call last):
  File "/Users/moqi/Documents/Code/dive-into-python3-practice/c03/p100_dic1.py", line 7, in <module>
    print(a_dict['mysql'])
KeyError: 'mysql'
"""
