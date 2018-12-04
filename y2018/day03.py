def get_input():
    return open("input_day03.txt").read()


def fill_grid(puzzle):
    # main calculation
    grid = [[0] * 1000 for _ in range(1000)]

    claims = parse_claims(puzzle.splitlines())

    for c in claims.values():
        apply_claim(grid, c)

    return grid, claims


def parse_claims(i):
    claims = {}
    for line in i:
        id, at, start, dimensions = line.split()
        assert at == "@"
        assert id.startswith("#")
        id = id[1:]

        x1, y1 = map(int, start[:-1].split(","))
        dx, dy = map(int, dimensions.split("x"))
        x2, y2 = x1 + dx, y1 + dy

        claims[id] = (x1, x2, y1, y2)

    return claims


def apply_claim(grid, c):
    for i, j in square_iterator(*c):
        grid[i][j] += 1


def square_iterator(x1, x2, y1, y2):
    return ((i, j) for i in range(x1, x2) for j in range(y1, y2))


def part1(grid):
    return sum(sum(1 for cell in line if cell > 1) for line in grid)


def part2(grid, claims):
    pass
    # todo


def main_method():
    grid, claims = fill_grid(get_input())
    print("Part 1:", part1(grid))
    print("Part 2:", part2(grid, claims))


if __name__ == "__main__":
    main_method()
