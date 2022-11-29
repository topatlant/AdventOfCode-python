from dataclasses import dataclass


@dataclass
class Passport:
    byr: str = None
    iyr: str = None
    eyr: str = None
    hgt: str = None
    hcl: str = None
    ecl: str = None
    pid: str = None
    cid: str = None


def get_input():
    with open("inputs/04.txt") as f:
        return [line.strip() for line in f.readlines()]


def main():
    print("Part1:", part1(get_input()))
    # print("Part2:", part2(get_input()))


def part1(puzzle):
    passports = parse(puzzle)
    return sum(is_valid(p) for p in passports)


def parse(puzzle) -> list[Passport]:
    passports = split_by_blanks(puzzle)
    return [parse_passport(p) for p in passports]


def split_by_blanks(lines: list[str]) -> list[list[str]]:
    res = []

    try:
        while lines:
            index = lines.index("")
            res.append(lines[:index])
            lines = lines[index + 1:]
    except ValueError:  # last group found
        res.append(lines)

    return res


def parse_passport(p: list[str]) -> Passport:
    res = Passport()
    for token in get_tokens(p):
        setattr(res, token[0], token[1])
    return res


def get_tokens(p: list[str]):
    for line in p:
        for key_value in line.split():
            yield key_value.split(":")


def is_valid(p: Passport) -> bool:
    for a in ("byr", "iyr", "eyr",
              "hgt", "hcl", "ecl", "pid"):  # , "cid"):
        if not getattr(p, a):
            return False
    return True


if __name__ == "__main__":
    main()
