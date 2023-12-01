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
    tokens = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    return list(digits_in(line, tokens))


def to_digits_from_right(line: str) -> list[int]:
    # just reverse every string and check from left, as usual
    tokens = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tokens_reversed = [t[::-1] for t in tokens]
    return list(digits_in(line[::-1], tokens_reversed))


def digits_in(line: str, tokens: list[str]) -> Iterator[int]:
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


if __name__ == "__main__":
    main()
