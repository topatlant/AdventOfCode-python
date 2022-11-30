import hashlib


def get_input():
    return "iwrupvqb"


def main():
    print("Part 1:", part1(get_input()))
    print("Part 2:", part2(get_input()))


def part1(puzzle):
    return hash_with_n_leading_spaces(puzzle, 5)


def part2(puzzle):
    return hash_with_n_leading_spaces(puzzle, 6)


def hash_with_n_leading_spaces(x, n):
    i = 1

    while True:
        result = hashlib.md5((x + str(i)).encode("ascii")).hexdigest()
        if result.startswith("0" * n):
            return i

        i += 1


if __name__ == "__main__":
    main()
