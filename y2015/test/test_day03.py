from y2015.day03 import *


def test_part1():
    i = ((">", 2), ("^>v<", 4), ("^v^v^v^v^v", 2))
    for tc in i:
        assert part1(tc[0]) == tc[1]


def test_part2():
    i = (("^v", 3), ("^>v<", 3), ("^v^v^v^v^v", 11))
    for tc in i:
        assert part2(tc[0]) == tc[1]
