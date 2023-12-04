from y2023.day03 import *

puzzle = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".splitlines()


def test_part1():
    assert part1(puzzle) == 4361


def test_part2():
    assert part2(puzzle) == 467835
