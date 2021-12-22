from y2021.day03 import *

i = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""


def test_part1():
    assert part1(i) == 198


def test_part2():
    assert part2(i) == 230
