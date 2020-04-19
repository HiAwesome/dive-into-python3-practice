query = 'user=username&database=mysql&password=88888888'

a_list = query.split('&')
print(a_list)
print()

a_list_of_lists = [v.split('=', 1) for v in a_list]
print(a_list_of_lists)
print()

a_dict = dict(a_list_of_lists)
print(a_dict)

"""
/usr/local/bin/python3 /Users/moqi/Documents/Code/dive-into-python3-practice/c05/p145_query_split.py
['user=username', 'database=mysql', 'password=88888888']

[['user', 'username'], ['database', 'mysql'], ['password', '88888888']]

{'user': 'username', 'database': 'mysql', 'password': '88888888'}

Process finished with exit code 0
"""
