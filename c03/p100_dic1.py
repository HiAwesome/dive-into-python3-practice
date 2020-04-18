a_dict = {'server': 'db.div.org', 'db': 'mysql'}
print(a_dict)

print(a_dict['db'])
print(a_dict['server'])

try:
    print(a_dict['mysql'])
except KeyError as err:
    print('The key %s is not exist now' % err)

print()
a_dict['user'] = 'mark'
print(a_dict)
a_dict['user'] = 'dora'
print(a_dict)
a_dict['User'] = 'Tom Smith'
print(a_dict)

"""
{'server': 'db.div.org', 'db': 'mysql'}
mysql
db.div.org
The key 'mysql' is not exist now

{'server': 'db.div.org', 'db': 'mysql', 'user': 'mark'}
{'server': 'db.div.org', 'db': 'mysql', 'user': 'dora'}
{'server': 'db.div.org', 'db': 'mysql', 'user': 'dora', 'User': 'Tom Smith'}
"""
