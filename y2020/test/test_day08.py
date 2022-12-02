from y2020.day08 import *

puzzle = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""".splitlines()


def test_part1():
    assert part1(puzzle) == 5


def test_part2():
    assert part2(puzzle) == 8
