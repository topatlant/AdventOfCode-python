from y2020.day03 import *


def test_part1():
    puzzle = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""".splitlines()
    assert part1(puzzle) == 7



# def test_part2():
#    assert sum(conforms_part2(*parse_pw_policy(line)) for line in puzzle) == 1
