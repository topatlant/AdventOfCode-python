from y2022.day03 import *

puzzle = [
    line.strip()
    for line in """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".splitlines()
]


def test_part1():
    assert part1(puzzle) == 157


def test_part2():
    assert part2(puzzle) == 70
