from y2021.day02 import *

i = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


def test_part1():
    assert part1(i) == 150


def test_part2():
    assert part2(i) == 900
