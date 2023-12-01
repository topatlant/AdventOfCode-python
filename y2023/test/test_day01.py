from y2023.day01 import *


def test_part1():
    puzzle = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".splitlines()
    assert part1(puzzle) == 142


def test_to_digits():
    assert to_digits("two1nine") == [2, 1, 9]
    assert to_digits("eightwothree") == [8, 3]
    assert to_digits("abcone2threexyz") == [1, 2, 3]
    assert to_digits("on5afa") == [5]
    assert to_digits("abeight9a") == [8, 9]
    assert to_digits("hthphptmmtwo7sixsevenoneightls") == [2, 7, 6, 7, 1]


def test_to_digits_from_right():
    assert to_digits_from_right("hthphptmmtwo7sixsevenoneightls") == [8, 7, 6, 7, 2]


def test_part2():
    puzzle = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".splitlines()
    assert part2(puzzle) == 281
