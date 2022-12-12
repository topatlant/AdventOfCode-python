from y2022.day12 import *


def test_part1():
    puzzle = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
""".splitlines()
    assert part1(puzzle) == 31


def test_part2():
    puzzle = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
""".splitlines()
    assert part2(puzzle) == 29
