import re


def match_sxz(noun):
    return re.search('[sxz]$', noun)


def apply_sxz(noun):
    return re.sub('$', 'es', noun)


def match_h(noun):
    return re.search('[^aeioudgkprt]h$', noun)


def apply_h(noun):
    return re.sub('$', 'es', noun)


def match_y(noun):
    return re.search('[^aeiou]y$', noun)


def apply_y(noun):
    return re.sub('y$', 'ies', noun)


# 对应的应用规则作为默认总是被应用，放在元祖的最后位置
# noinspection PyUnusedLocal
def match_default(noun):
    return True


def apply_default(noun):
    return noun + 's'


# 一系列函数对
rules = (
    (match_sxz, apply_sxz),
    (match_h, apply_h),
    (match_y, apply_y),
    (match_default, apply_default)
)


def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)


# plural 函数展开
def plural_unfold(noun):
    if match_sxz(noun):
        return apply_sxz(noun)
    if match_h(noun):
        return apply_h(noun)
    if match_y(noun):
        return apply_y(noun)
    if match_default(noun):
        return apply_default(noun)
