from y2015.day01 import *


def test_part1():
    i = (
        ("()()", 0),
        ("(())", 0),
        ("(((", 3),
        ("(()(()(", 3),
        ("))(((((", 3),
        ("())", -1),
        ("))(", -1),
        (")))", -3),
        (")())())", -3)
    )
    for tc in i:
        assert part1(tc[0]) == tc[1]


def test_part2():
    i = (
        (")", 1),
        ("()())", 5)
    )
    for tc in i:
        assert part2(tc[0]) == tc[1]
