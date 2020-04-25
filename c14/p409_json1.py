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
print('json dump successful.')
