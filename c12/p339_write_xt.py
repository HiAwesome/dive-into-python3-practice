from file_path_collect import output_txt_path_dir

log_path = output_txt_path_dir + 'test.log'
with open(log_path, mode='w', encoding='utf-8') as a_file:
    a_file.write('test successed')

with open(log_path, encoding='utf-8') as a_file:
    print(a_file.read())

with open(log_path, mode='a', encoding='utf-8') as a_file:
    a_file.write(' and again')

with open(log_path, encoding='utf-8') as a_file:
    print(a_file.read())

"""
test successed
test successed and again
"""
