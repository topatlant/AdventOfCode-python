from y2022.day01 import *

puzzle = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000""".splitlines()


def test_part1():
    assert part1(puzzle) == 24000


def test_part2():
    assert part2(puzzle) == 45000
