from y2020.day02 import *

puzzle = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc""".splitlines()


def test_part1():
    assert sum(conforms_part1(*parse_pw_policy(line)) for line in puzzle) == 2


def test_part2():
    assert sum(conforms_part2(*parse_pw_policy(line)) for line in puzzle) == 1
