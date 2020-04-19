import re


def build_match_add_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)

    def apply_rule(word):
        return re.sub(search, replace, word)

    # 返回元组，所以括号不去掉
    return (matches_rule, apply_rule)


rules = []

with open('../resource/txt/plural4-rules.txt', encoding='utf-8') as pattern_file:
    for line in pattern_file:
        # 用 None 切割，表示对任何空白字符进行分隔
        pattern, search, replace = line.split(None, 3)
        rules.append(build_match_add_apply_functions(pattern, search, replace))
