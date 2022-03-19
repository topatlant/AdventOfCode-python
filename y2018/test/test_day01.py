from y2018.day01 import *


def to_input_format(i):
    return i.replace(", ", "\n")


def test_part1():
    i = (
        ("+1, -2, +3, +1", 3),
        ("+1, +1, +1", 3),
        ("+1, +1, -2", 0),
        ("-1, -2, -3", -6),
    )
    for tc in i:
        assert part1(to_input_format(tc[0])) == tc[1]


def test_part2():
    i = (
        ("+1, -2, +3, +1", 2),
        ("+1, -1", 0),
        ("+3, +3, +4, -2, -4", 10),
        ("-6, +3, +8, +5, -6", 5),
        ("+7, +7, -2, -7, -4", 14),
    )
    for tc in i:
        assert part2(to_input_format(tc[0])) == tc[1]
