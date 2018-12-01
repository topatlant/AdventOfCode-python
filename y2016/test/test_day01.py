from y2016.day01 import *


def test_part1():
    i = (("R2, L3", 5), ("R2, R2, R2", 2), ("R5, L5, R5, R3", 12))
    for tc in i:
        assert part1(tc[0]) == tc[1]


def test_part2():
    assert part2("R8, R4, R4, R8") == 4

