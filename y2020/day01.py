import itertools


def get_input() -> list[int]:
    with open("inputs/01.txt") as f:
        return [int(d) for d in f]


def main():
    print("Part 1:", part1(get_input()))
    print("Part 2:", part2(get_input()))


def part1(puzzle):
    for x, y in itertools.combinations(puzzle, 2):
        if x + y == 2020:
            print(f"{x} * {y} = {x * y}")
            return x * y


def part2(puzzle):
    for x, y, z in itertools.combinations(puzzle, 3):
        if x + y + z == 2020:
            print(f"{x} * {y} * {z} = {x * y * z}")
            return x * y * z


if __name__ == "__main__":
    main()
