from file_path_collect import favorite_people_txt_path as path

line_number = 0

with open(path, encoding='utf-8') as a_file:
    for a_line in a_file:
        line_number += 1
        """
        格式说明符{:>4}的意思是"使用最多四个空格使之右对齐，然后打印此参数。
        字符串方法 rstrip() 可以去掉尾随的空白符，包括回车符。
        """
        print('{:>4} {}'.format(line_number, a_line.rstrip()))

"""
   1 Dora
   2 Ethan
   3 Wesley
   4 John
   5 Anne
   6 Mike
   7 Chris
   8 Sarah
   9 Alex
  10 Lizzie
"""
