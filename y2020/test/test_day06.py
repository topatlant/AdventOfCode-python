from y2020.day06 import *

puzzle = """abc

a
b
c

ab
ac

a
a
a
a

b""".splitlines()


def test_part1():
    assert part1(puzzle) == 11


def test_part2():
    assert part2(puzzle) == 6
