from y2022.day12 import *

puzzle = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
""".splitlines()


def test_part1():
    assert part1(puzzle) == 31
