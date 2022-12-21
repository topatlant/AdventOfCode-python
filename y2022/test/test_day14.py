from y2022.day14 import *

puzzle = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""".splitlines()


def test_part1():
    assert part1(puzzle) == 24


def test_part2():
    assert part2(puzzle) == 93
