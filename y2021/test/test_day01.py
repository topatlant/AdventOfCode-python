from y2021.day01 import *


def to_input_format(x):
    return x.replace(",", "\n")


def test_part1():
    i = "199,200,208,210,200,207,240,269,260,263"
    assert part1(to_input_format(i)) == 7


def test_part2():
    i = "199,200,208,210,200,207,240,269,260,263"
    assert part2(to_input_format(i)) == 5
