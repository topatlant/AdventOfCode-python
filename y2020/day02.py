from dataclasses import dataclass

data = open("input_day02.txt").readlines()


@dataclass
class Policy:
    letter: str
    n1: int
    n2: int


def parse_pw_policy(line):
    pol, pw = line.strip().split(":")
    pw = pw.strip()
    minmax, letter = pol.split()
    letter = letter.strip()
    min, max = minmax.split('-')
    return pw, Policy(letter, int(min), int(max))


def conforms_part1(pw: str, p: Policy):
    c = pw.count(p.letter)
    return p.n1 <= c <= p.n2


def conforms_part2(pw: str, p: Policy):
    letter_1_correct = pw[p.n1 - 1] == p.letter
    letter_2_correct = pw[p.n2 - 1] == p.letter
    return letter_1_correct != letter_2_correct


counter1 = counter2 = 0
for line in data:
    password, policy = parse_pw_policy(line)
    if conforms_part1(password, policy):
        counter1 += 1
    if conforms_part2(password, policy):
        counter2 += 1

print(f"Part1 policy: {counter1} valid passwords")
print(f"Part2 policy: {counter2} valid passwords")
