from y2022.day02 import *

puzzle = """A Y
B X
C Z""".splitlines()


def test_part1():
    assert part1(puzzle) == 15
    # assert part1(get_input())==12645


def test_part2():
    assert part2(puzzle) == 12
