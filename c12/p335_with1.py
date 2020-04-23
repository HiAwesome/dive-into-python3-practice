from file_path_collect import chinese_txt_path

"""
从技术上说，with语句创建了一个运行时环境(runtimecontext)。
在这几个样例中，流对象的行为就像一个上下文管理器(contextmanager)。Python创建了a_file，并且告诉它正进入一个运行时环境。
当with块结束的时候，Python告诉流对象它正在退出这个运行时环境，然后流对象就会调用它的close()方法。
"""
with open(chinese_txt_path, encoding='utf-8') as a_file:
    a_file.seek(17)
    a_character = a_file.read(1)
    print(a_character)

"""
是
"""
