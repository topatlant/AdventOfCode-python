from typing import Iterator


def get_input():
    with open("inputs/01.txt") as f:
        return f.readlines()


def main():
    puzzle = get_input()
    print("Part 1:", part1(puzzle))
    print("Part 2:", part2(puzzle))


def part1(puzzle: list[str]) -> int:
    cal_values = [10 * digits(line)[0] + digits(line)[-1] for line in puzzle]
    return sum(cal_values)


def part2(puzzle: list[str]) -> int:
    cal_values = [
        10 * to_digits(line)[0] + to_digits_from_right(line)[0] for line in puzzle
    ]
    return sum(cal_values)


def digits(line: str) -> list[int]:
    return [int(x) for x in line if x.isdigit()]


def to_digits(line: str) -> list[int]:
    return list(digits_in(line))


def to_digits_from_right(line: str) -> list[int]:
    return list(digits_from_right_in(line))


def digits_in(line: str) -> Iterator[int]:
    tokens = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    while line:

        if line[0].isdigit():
            yield int(line[0])
            line = line[1:]
            continue

        for n in tokens:
            if line.startswith(n):
                yield tokens.index(n) + 1
                line = line[len(n) :]
                break
        else:
            # string starts with neither of the numbers
            line = line[1:]


def digits_from_right_in(line) -> Iterator[int]:
    tokens = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    while line:

        if line[-1].isdigit():
            yield int(line[-1])
            line = line[:-1]
            continue

        for n in tokens:
            if line.endswith(n):
                yield tokens.index(n) + 1
                line = line[: -len(n)]
                break
        else:
            # string ends with neither of the numbers
            line = line[:-1]


if __name__ == "__main__":
    main()
