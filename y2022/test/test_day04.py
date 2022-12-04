from y2022.day04 import *

puzzle = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""".splitlines()


def test_part1():
    assert part1(puzzle) == 2


def test_part2():
    assert part2(puzzle) == 4
