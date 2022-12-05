from y2022.day05 import *

initial_state = """    [D]
[N] [C]
[Z] [M] [P]
 1   2   3""".splitlines()
instructions = """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""".splitlines()


def test_part1():
    assert part1(initial_state, instructions) == "CMZ"


def test_part2():
    assert part2(initial_state, instructions) == "MCD"


def test_parse_initial_state():
    expected = [["Z", "N"], ["M", "C", "D"], ["P"]]
    assert parse_initial_state(initial_state) == expected


def test_perform_action():
    stacks = [["Z", "N"], ["M", "C", "D"], ["P"]]

    action = "move 1 from 2 to 1"
    expected = [["Z", "N", "D"], ["M", "C"], ["P"]]
    perform_action(stacks, action)
    assert stacks == expected

    action = "move 3 from 1 to 3"
    expected = [[], ["M", "C"], ["P", "D", "N", "Z"]]
    perform_action(stacks, action)
    assert stacks == expected
