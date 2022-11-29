from dataclasses import dataclass
import re


def get_input():
    with open("inputs/04.txt") as f:
        return [line.strip() for line in f.readlines()]


def main():
    print("Part1:", part1(get_input()))
    print("Part2:", part2(get_input()))


def part1(puzzle):
    passports = parse(puzzle)
    return sum(is_valid_part1(p) for p in passports)


def part2(puzzle):
    passports = parse(puzzle)
    return sum(is_valid_part2(p) for p in passports)


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

    def required_fields_are_present(self):
        for a in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"):  # cid is ignored
            if not getattr(self, a):
                return False
        return True

    def all_fields_are_valid(self):
        if not self.required_fields_are_present():
            return False
        for a in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"):  # cid is ignored
            if not getattr(self, f"validate_{a}")(getattr(self, a)):
                return False
        return True

    @staticmethod
    def validate_byr(year: str):
        if len(year) != 4:
            return False
        try:
            y = int(year)
            return 1920 <= y <= 2002
        except ValueError:
            return False

    @staticmethod
    def validate_iyr(year: str):
        if len(year) != 4:
            return False
        try:
            y = int(year)
            return 2010 <= y <= 2020
        except ValueError:
            return False

    @staticmethod
    def validate_eyr(year: str):
        if len(year) != 4:
            return False
        try:
            y = int(year)
            return 2020 <= y <= 2030
        except ValueError:
            return False

    @staticmethod
    def validate_hgt(height: str):
        try:
            h = int(height[:-2])
            if height.endswith("cm"):
                return 150 <= h <= 193
            elif height.endswith("in"):
                return 59 <= h <= 76
            else:
                return False
        except ValueError:
            return False

    @staticmethod
    def validate_hcl(color: str):
        return len(color) == 7 and re.match("#[0-9a-f]{6}", color)

    @staticmethod
    def validate_ecl(color: str):
        return color in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")

    @staticmethod
    def validate_pid(pid: str):
        return len(pid) == 9 and re.match("[0-9]{9}", pid)


def parse(puzzle) -> list[Passport]:
    passports = split_by_blanks(puzzle)
    return [parse_passport(p) for p in passports]


def split_by_blanks(lines: list[str]) -> list[list[str]]:
    res = []

    try:
        while lines:
            index = lines.index("")
            res.append(lines[:index])
            lines = lines[index + 1 :]
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


def is_valid_part1(p: Passport) -> bool:
    return p.required_fields_are_present()


def is_valid_part2(p: Passport) -> bool:
    return p.all_fields_are_valid()


if __name__ == "__main__":
    main()
