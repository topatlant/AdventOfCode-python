from y2022.day08 import *

puzzle = """30373
25512
65332
33549
35390""".splitlines()


def test_part1():
    assert part1(puzzle) == 21


def test_part2():
    assert part2(puzzle) == 8
