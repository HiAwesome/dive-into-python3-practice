import re
import sys


def build_match_add_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)

    def apply_rule(word):
        return re.sub(search, replace, word)

    # 返回元组，所以括号不去掉
    return (matches_rule, apply_rule)


def rules(rules_filename):
    with open(rules_filename, encoding='utf-8') as pattern_file:
        for line in pattern_file:
            pattern, search, replace = line.split(None, 3)
            yield build_match_add_apply_functions(pattern, search, replace)


def plural(noun, rules_filename='../resource/txt/plural5-rules.txt'):
    for matches_rule, apply_rule in rules(rules_filename):
        if matches_rule(noun):
            return apply_rule(noun)

    raise ValueError('no matching rule for {0}'.format(noun))


if __name__ == '__main__':

    if sys.argv[1:]:
        print(plural(sys.argv[1]))
    else:
        print(__doc__)

"""
在本目录命令行执行以下代码：
-> % python3 p202_plural5.py hello
hellos
-> % python3 p202_plural5.py agency
agencies
-> % python3 p202_plural5.py coach 
coaches
-> % python3 p202_plural5.py hours
hourses
"""
