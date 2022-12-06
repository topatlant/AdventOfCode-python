from y2017.day02 import *


def test_part1():
    puzzle = """5 1 9 5
7 5 3
2 4 6 8""".splitlines()
    assert part1(puzzle) == 18


def test_part2():
    puzzle = """5 9 2 8
9 4 7 3
3 8 6 5""".splitlines()
    assert part2(puzzle) == 9
