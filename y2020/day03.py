import numpy as np


def get_input():
    with open("inputs/03.txt") as f:
        return [line.strip() for line in f]


def main():
    print("Part1:", part1(get_input()))


def part1(puzzle):
    grid = parse(puzzle)
    return sum(traverse(grid))


def parse(puzzle):
    height = len(puzzle)
    width = len(puzzle[0])
    grid = np.zeros([height, width], dtype=bool)
    for x, line in enumerate(puzzle):
        for y, char in enumerate(line):
            if char == "#":
                grid[x, y] = True  # that's a tree
            elif char != ".":
                raise ValueError("invalid character encountered")
    return grid


def traverse(grid):
    for x in range(grid.shape[0]):
        yield grid[x, (x * 3) % grid.shape[1]]


if __name__ == "__main__":
    main()
