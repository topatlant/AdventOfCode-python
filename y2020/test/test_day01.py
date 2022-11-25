from y2020.day01 import *

puzzle = [1721, 979, 366, 299, 675, 1456]


def test_part1():
    assert part1(puzzle) == 1721 * 299


def test_part2():
    assert part2(puzzle) == 979 * 366 * 675
