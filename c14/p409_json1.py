import json

from file_path_collect import output_json_path_dir as output

basic_entry = {
    'id': 256,
    'title': 'Dive into history, 2009 edition',
    'tags': ('diveintopython', 'docbook', 'html'),
    'published': True,
    'comments_link': None
}

with open(output + 'basic.json', mode='w', encoding='utf-8') as f:
    json.dump(basic_entry, f)
print('basic json dump successful.')

"""
如果你给json.dump()函数传入indent参数,它以文件变大为代价使生成的JSON文件更可读。
indent参数是一个整数。0意味着“每个值单独一行。
”大于0的数字意味着“每个值单独一行并且使用这个数目的空格来缩进嵌套的数据结构。”
"""
with open(output + 'basic_with_indent.json', mode='w', encoding='utf-8') as f:
    json.dump(basic_entry, f, indent=2)
print('basic_with_indent json dump successful.')
