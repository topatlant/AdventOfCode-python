from y2022.day09 import *

puzzle = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".splitlines()


def test_part1():
    assert part1(puzzle) == 13
