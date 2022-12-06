def get_input():
    with open("inputs/06.txt") as f:
        return f.read()


def main():
    puzzle = get_input()
    print("Part 1:", part1(puzzle))
    print("Part 2:", part2(puzzle))


def part1(puzzle: str) -> int:
    return marker_of_length(puzzle, 4)


def part2(puzzle: str) -> int:
    return marker_of_length(puzzle, 14)


def marker_of_length(message: str, length: int) -> int:
    for i in range(length, len(message) + 1):
        substr = message[i - length : i]
        if len(set(substr)) == length:
            return i


if __name__ == "__main__":
    main()
