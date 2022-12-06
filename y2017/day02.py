from itertools import permutations


def get_input():
    with open("inputs/02.txt") as f:
        return f.readlines()


def main():
    puzzle = get_input()
    print("Part 1:", part1(puzzle))
    print("Part 2:", part2(puzzle))


def part1(rows: list[str]) -> int:
    return sum(checksum1(row) for row in rows)


def part2(rows: list[str]) -> int:
    return sum(checksum2(row) for row in rows)


def checksum1(row: str) -> int:
    numbers = [int(x) for x in row.split()]
    return max(numbers) - min(numbers)


def checksum2(row: str) -> int:
    numbers = [int(x) for x in row.split()]

    for x, y in permutations(numbers, 2):
        if x > y and x % y == 0:
            return x // y


if __name__ == "__main__":
    main()
