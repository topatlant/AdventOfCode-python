import numpy as np


def get_input() -> list[str]:
    with open("inputs/03.txt") as f:
        return [line.strip() for line in f]


def main():
    puzzle = get_input()
    print("Part1:", part1(puzzle))
    print("Part2:", part2(puzzle))


def part1(puzzle):
    grid = parse(puzzle)
    return sum(traverse(grid, slope=(3, 1)))


def part2(puzzle):
    grid = parse(puzzle)
    res = 1
    for slope in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
        n_trees = sum(traverse(grid, slope))
        print(f"with slope {slope} we encounter {n_trees} trees")
        res *= n_trees
    return res


def parse(puzzle) -> np.ndarray:
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


def traverse(grid: np.ndarray, slope: tuple[int, int]):
    x = y = 0
    while x < grid.shape[0]:
        yield grid[x, y]
        x += slope[1]
        y = (y + slope[0]) % grid.shape[1]


if __name__ == "__main__":
    main()
