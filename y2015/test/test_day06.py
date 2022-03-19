from y2015.day06 import *


def test_part1():
    l1, l2 = fill_lights("turn on 0,0 through 999,999")
    assert part1(l1) == 1000000

    l1, l2 = fill_lights("toggle 0,0 through 999,0")
    assert part1(l1) == 1000

    l1, l2 = fill_lights("turn off 499,499 through 500,500")
    assert part1(l1) == 0

    l1, l2 = fill_lights(
        """turn on 0,0 through 999,999
toggle 0,0 through 999,0
turn off 499,499 through 500,500"""
    )
    assert part1(l1) == 998996


def test_part2():
    l1, l2 = fill_lights("turn on 0,0 through 0,0")
    assert part2(l2) == 1
    l1, l2 = fill_lights("toggle 0,0 through 999,999")
    assert part2(l2) == 2000000
