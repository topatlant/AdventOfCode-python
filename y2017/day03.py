def get_input():
    return 325489


def main():
    puzzle = get_input()
    print("Part 1:", part1(puzzle))
    print("Part 2:", part2(puzzle))


def part1(number: int) -> int:
    # Manhattan distance
    coords = get_coords(number)
    return abs(coords[0]) + abs(coords[1])


def part2(threshold: int) -> int:
    grid = {(0, 0): 1}
    value = 1
    spiral_walk = spiral_iterator()

    while value <= threshold:
        coords = next(spiral_walk)
        value = sum(grid[(x, y)] for x, y in neighbors(coords) if (x, y) in grid)
        grid[coords] = value
    return value


def get_coords(n: int) -> tuple[int, int]:
    # I did not bother to rewrite the solution of part1
    # with the iterator from part2, because I like it so much ;)
    directions = walk_in_spiral(n)
    x = directions.count("r") - directions.count("l")
    y = directions.count("u") - directions.count("d")
    return x, y


def walk_in_spiral(n: int) -> str:
    """get a string of directions that takes you to the n-th position
    (starting from the origin == 1)"""
    k = 1
    res = ""
    while len(res) < n - 1:
        res += "r" * k  # right
        res += "u" * k  # up
        k += 1
        res += "l" * k  # left
        res += "d" * k  # down
        k += 1
    return res[: n - 1]


def spiral_iterator():
    x, y = 0, 0
    k = 1
    while True:
        for i in range(k):  # right
            x += 1
            yield x, y
        for i in range(k):  # up
            y += 1
            yield x, y
        k += 1
        for i in range(k):  # left
            x -= 1
            yield x, y
        for i in range(k):  # down
            y -= 1
            yield x, y
        k += 1


def neighbors(coord):
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            yield coord[0] + i, coord[1] + j


if __name__ == "__main__":
    main()
