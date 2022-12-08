from y2017.day03 import *


def test_part1():
    assert part1(1) == 0
    assert part1(12) == 3
    assert part1(23) == 2
    assert part1(1024) == 31


def test_part2():
    assert part2(800) == 806


def test_walk_in_spiral():
    assert walk_in_spiral(1) == ""
    assert walk_in_spiral(4) == "rul"
