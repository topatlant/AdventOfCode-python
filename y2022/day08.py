from common.itertools import take_until_first


def get_input():
    with open("inputs/08.txt") as f:
        return f.readlines()


def main():
    puzzle = get_input()
    print("Part 1:", part1(puzzle))
    print("Part 2:", part2(puzzle))


def part1(puzzle: list[str]) -> int:
    grid = parse(puzzle)
    max_x = len(grid[0])
    max_y = len(grid)
    return sum(is_visible(grid, x, y) for x in range(max_x) for y in range(max_y))


def part2(puzzle: list[str]) -> int:
    grid = parse(puzzle)
    max_x = len(grid[0])
    max_y = len(grid)
    return max(get_scenic_score(grid, x, y) for x in range(max_x) for y in range(max_y))


def parse(puzzle: list[str]) -> list[list[int]]:
    grid = [[int(x) for x in line.strip()] for line in puzzle]
    return grid


def is_visible(grid: list[list[int]], x: int, y: int) -> bool:
    max_x = len(grid[0]) - 1
    max_y = len(grid) - 1

    if x == 0 or x == max_x or y == 0 or y == max_y:
        # edge case ;)
        return True

    height = grid[y][x]
    return any(
        all(height > other for other in line_of_sight)
        for line_of_sight in get_lines_of_sight(grid, x, y)
    )


def get_lines_of_sight(grid: list[list[int]], x: int, y: int) -> list[list[int]]:
    # horizontal left and right, cut out position x
    row = grid[y]
    res = [row[x - 1 :: -1], row[x + 1 :]]

    # vertical up and down, cut out position y
    col = [line[x] for line in grid]
    res += [col[y - 1 :: -1], col[y + 1 :]]

    return res


def get_scenic_score(grid: list[list[int]], x: int, y: int) -> int:
    max_x = len(grid[0]) - 1
    max_y = len(grid) - 1

    if x == 0 or x == max_x or y == 0 or y == max_y:
        # edge case ;)
        return 0

    height = grid[y][x]
    scenic_score = 1

    for line_of_sight in get_lines_of_sight(grid, x, y):
        viewing_distance = len(
            list(take_until_first(lambda other: other >= height, line_of_sight))
        )
        scenic_score *= viewing_distance

    return scenic_score


if __name__ == "__main__":
    main()
