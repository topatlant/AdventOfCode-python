from y2020.day03 import *

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


def test_part1():
    assert part1(puzzle) == 7


def test_part2():
    assert part2(puzzle) == 336
