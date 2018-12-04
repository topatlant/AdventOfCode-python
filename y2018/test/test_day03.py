from y2018.day03 import *


def test_part1():
    i = """#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2"""
    grid, claims = fill_grid(i)
    assert part1(grid) == 4


def test_part2():
    i = """#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2"""
    grid, claims = fill_grid(i)
    assert part2(grid, claims) == 3
