from itertools import tee


def get_input():
    with open("inputs/05.txt") as f:
        return [line.strip() for line in f]


def main():
    puzzle = get_input()
    print("Part1:", part1(puzzle))
    print("Part2:", part2(puzzle))


def part1(puzzle):
    return max(get_seat_id(bp) for bp in puzzle)


def part2(puzzle):
    seat_ids = (get_seat_id(bp) for bp in puzzle)
    for x, y in pairwise(sorted(seat_ids)):
        if y - x == 2:
            print(x, y)
            return x + 1


def get_seat_id(boarding_pass: str) -> int:
    row, col = extract_row_col(boarding_pass)
    return row * 8 + col


def extract_row_col(boarding_pass: str):
    assert len(boarding_pass) == 10
    row = boarding_pass[:7]
    col = boarding_pass[7:]
    row = row.replace("F", "0")
    row = row.replace("B", "1")
    col = col.replace("R", "1")
    col = col.replace("L", "0")
    return int(row, base=2), int(col, base=2)


def pairwise(iterable):
    """s -> (s0,s1), (s1,s2), (s2, s3), ..."""
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


if __name__ == "__main__":
    main()
