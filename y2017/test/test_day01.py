from y2017.day01 import *


def test_part1():
    i = (
        ("1122", 3),
        ("1111", 4),
        ("1234", 0),
        ("91212129", 9)
    )
    for tc in i:
        assert part1(tc[0]) == tc[1]


def test_part2():
    i = (
        ("1212", 6),
        ("1221", 0),
        ("123425", 4),
        ("123123", 12),
        ("12131415", 4)
    )
    for tc in i:
        assert part2(tc[0]) == tc[1]
