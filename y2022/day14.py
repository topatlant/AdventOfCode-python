import numpy as np
from typing import Iterator
from dataclasses import dataclass
from common.itertools import pairwise


def get_input():
    with open("inputs/14.txt") as f:
        return f.readlines()


def main():
    puzzle = get_input()
    print("Part 1:", part1(puzzle))
    print("Part 2:", part2(puzzle))


def part1(puzzle) -> int:
    return part1_and_2(puzzle, pt2=False)


def part2(puzzle) -> int:
    return part1_and_2(puzzle, pt2=True)


def part1_and_2(puzzle, pt2: bool) -> int:
    all_rocks = parse(puzzle)

    y_floor = max(p[1] for p in all_rocks) + 2

    grid = np.zeros([2000, y_floor], "?")
    for p in all_rocks:
        grid[p] = True

    n_sand = 0
    while drop_sand(grid, y_floor, pt2=pt2):
        n_sand += 1

    return n_sand


coordinates = tuple[int, int]


@dataclass
class StraightLine:
    start: coordinates
    end: coordinates


def parse(puzzle) -> list[coordinates]:
    all_rocks = [
        rock
        for line_of_rock in get_lines_from_puzzle(puzzle)
        for rock in get_points(line_of_rock)
    ]
    return all_rocks


def get_lines_from_puzzle(puzzle: list[str]) -> Iterator[StraightLine]:
    for line_of_string in puzzle:

        coords = line_of_string.split(" -> ")
        for start, end in pairwise(coords):
            x1, y1 = start.split(",")
            x2, y2 = end.split(",")
            yield StraightLine((int(x1), int(y1)), (int(x2), int(y2)))


def get_points(line: StraightLine) -> Iterator[coordinates]:
    x1, x2 = line.start[0], line.end[0]
    y1, y2 = line.start[1], line.end[1]
    if x1 == x2:
        a = min(y1, y2)
        b = max(y1, y2)
        yield from [(x1, y) for y in range(a, b + 1)]
    else:
        a = min(x1, x2)
        b = max(x1, x2)
        yield from [(x, y1) for x in range(a, b + 1)]


def drop_sand(grid: np.array, y_floor: int, pt2: bool) -> bool:
    """:return: whether to continue dropping sand"""

    x, y = 500, 0

    if grid[x, y]:
        return False  # reaching the source

    while True:

        if y + 1 == y_floor:
            grid[x, y] = True
            return pt2  # in pt1 we stop when reaching the floor

        if not grid[x, y + 1]:
            # step down
            y += 1
            continue

        if not grid[x - 1, y + 1]:
            # down left
            x -= 1
            y += 1
            continue

        if not grid[x + 1, y + 1]:
            # down right
            x += 1
            y += 1
            continue

        # stay and settle
        grid[x, y] = True
        return True


if __name__ == "__main__":
    main()
