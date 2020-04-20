"""
像这样的谜题被称为cryptarithms或者字母算术(alphametics)。
字母可以拼出实际的单词，而如果你把每一个字母都用0–9中的某一个数字代替后,也同样可以#8220;拼出”一个算术等式。
关键的地方是找出每个字母都映射到了哪个数字。每个字母所有出现的地方都必须映射到同一个数字，数字不能重复,并且“单词”不能以0开始。
最著名的字母算术谜题是SEND+MORE=MONEY。
在这一章中，我们将深入一个最初由RaymondHettinger编写的难以置信的Python程序。这个程序只用14行代码来解决字母算术谜题。
"""
import itertools
import re


def solve(puzzle):
    words = re.findall('[A-Z]+', puzzle.upper())
    unique_characters = set(''.join(words))
    assert len(unique_characters) <= 10, 'Too many letters'

    first_letters = {word[0] for word in words}
    n = len(first_letters)
    sorted_characters = ''.join(first_letters) + ''.join(unique_characters - first_letters)
    characters = tuple(ord(c) for c in sorted_characters)
    digits = tuple(ord(c) for c in '0123456789')
    zero = digits[0]

    for guess in itertools.permutations(digits, len(characters)):
        if zero not in guess[:n]:
            equation = puzzle.translate(dict(zip(characters, guess)))
            if eval(equation):
                return equation


if __name__ == '__main__':
    import sys

    for puzzle in sys.argv[1:]:
        print(puzzle)
        solution = solve(puzzle)
        if solution:
            print(solution)

"""
-> % python3 p228_alphametics.py "HAWAII + IDAHO + IOWA + OHIO == STATES"
HAWAII + IDAHO + IOWA + OHIO == STATES
510199 + 98153 + 9301 + 3593 == 621246
-> % python3 p228_alphametics.py "I + LOVE + YOU == DORA"
I + LOVE + YOU == DORA
3 + 1458 + 946 == 2407
-> % python3 p228_alphametics.py "SEND + MORE == MONEY"
SEND + MORE == MONEY
9567 + 1085 == 10652
"""
