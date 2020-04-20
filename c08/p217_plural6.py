import re
import sys


def build_match_add_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)

    def apply_rule(word):
        return re.sub(search, replace, word)

    # 返回元组，所以括号不去掉
    return (matches_rule, apply_rule)


class LazyRules:
    rules_filename = '../resource/txt/plural6-rules.txt'

    def __init__(self):
        self.pattern_file = open(self.rules_filename, encoding='utf-8')
        self.cache = []

    def __iter__(self):
        self.cache_index = 0
        return self

    def __next__(self):
        self.cache_index += 1
        if len(self.cache) >= self.cache_index:
            return self.cache[self.cache_index - 1]

        if self.pattern_file.closed:
            return StopIteration

        line = self.pattern_file.readline()
        if not line:
            self.pattern_file.close()
            raise StopIteration

        pattern, search, replace = line.split(None, 3)
        funcs = build_match_add_apply_functions(
            pattern, search, replace)
        self.cache.append(funcs)
        return funcs


rules = LazyRules()


def plural(noun):
    """Enter a noun to get the plural form"""
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)


if __name__ == '__main__':

    if sys.argv[1:]:
        print(plural(sys.argv[1]))
    else:
        print(plural.__doc__)

"""
在本目录命令行执行以下代码：
-> % python3 p217_plural6.py names
nameses
-> % python3 p217_plural6.py home 
homes
-> % python3 p217_plural6.py agency
agencies
-> % python3 p217_plural6.py sheep 
sheep
-> % python3 p217_plural6.py mouse     
mice
-> % python3 p217_plural6.py child
children
-> % python3 p217_plural6.py foot 
feet
"""
