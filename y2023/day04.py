def get_input():
    with open("inputs/04.txt") as f:
        return f.readlines()


def main():
    puzzle = get_input()
#     puzzle = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".splitlines()

    print("Part 1:", part1(puzzle))
    print("Part 2:", part2(puzzle))


def part1(puzzle) -> int:
    return sum(get_card_points(line) for line in puzzle)


def part2(puzzle) -> int:

    n_cards = [1] * len(puzzle)

    for i, line in enumerate(puzzle):
        n_wins = n_winning_numbers(line)
        n_copies = n_cards[i]
        for j in range(n_wins):
            n_cards[i + 1 + j] += n_copies

    return sum(n_cards)


def n_winning_numbers(line: str) -> int:
    winning_numbers = set(int(x) for x in line.split(":")[1].split("|")[0].split())
    our_numbers = set(int(x) for x in line.split(":")[1].split("|")[1].split())
    return len(winning_numbers.intersection(our_numbers))


def get_card_points(line: str) -> int:
    n_wins = n_winning_numbers(line)

    if n_wins == 0:
        return 0

    return 2 ** (n_wins - 1)


if __name__ == "__main__":
    main()
