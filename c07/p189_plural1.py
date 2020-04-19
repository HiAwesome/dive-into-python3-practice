import re


def plural(noun):
    if re.search('[xcz]$', noun):
        return re.sub('$', 'es', noun)
    elif re.search('[^aeioudgkprt]h$', noun):
        return re.sub('$', 'es', noun)
    elif re.search('[^aeiouy]y$', noun):
        return re.sub('y$', 'ies', noun)
    else:
        return noun + 's'


print(re.search('[abc]', 'Mark'))
print(re.sub('[abc]', 'o', 'Mark'))
print(re.sub('[abc]', 'o', 'rock'))
print(re.sub('[abc]', 'o', 'caps'))
print()

print(re.search('[^aeiou]y$', 'vacancy'))
print(re.search('[^aeiou]y$', 'boy'))
print(re.search('[^aeiou]y$', 'day'))
print(re.search('[^aeiou]y$', 'pita'))
print()

print(re.sub('y$', 'ies', 'vacancy'))
print(re.sub('y$', 'ies', 'agency'))
print(re.sub('([^aeiou])y$', r'\1ies', 'vancancy'))
print()

"""
<re.Match object; span=(1, 2), match='a'>
Mork
rook
oops

<re.Match object; span=(5, 7), match='cy'>
None
None
None

vacancies
agencies
vancancies

"""
