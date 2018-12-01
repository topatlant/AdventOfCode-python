from y2018 import day01


def to_input_format(i):
    return i.replace(", ", "\n")


def test_part1():
    i = to_input_format("+1, -2, +3, +1")
    assert day01.part1(i) == 3

    i = to_input_format("+1, +1, +1")
    assert day01.part1(i) == 3

    i = to_input_format("+1, +1, -2")
    assert day01.part1(i) == 0

    i = to_input_format("-1, -2, -3")
    assert day01.part1(i) == -6


def test_part2():
    i = to_input_format("+1, -2, +3, +1")
    assert day01.part2(i) == 2

    i = to_input_format("+1, -1")
    assert day01.part2(i) == 0

    i = to_input_format("+3, +3, +4, -2, -4")
    assert day01.part2(i) == 10

    i = to_input_format("-6, +3, +8, +5, -6")
    assert day01.part2(i) == 5

    i = to_input_format("+7, +7, -2, -7, -4")
    assert day01.part2(i) == 14
