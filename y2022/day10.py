from common import split_by_blanks


def get_input():
    with open("inputs/10.txt") as f:
        return f.readlines()


def main():
    puzzle = get_input()
    print("Part 1:", part1(puzzle))
    print("Part 2:")
    print(part2(puzzle))


def part1(puzzle: list[str]) -> int:
    values_during = execute_instructions(puzzle)
    return extract_interesting_signal_strenghts(values_during)


def part2(puzzle: list[str]) -> str:
    values_during = execute_instructions(puzzle)
    crt = ""
    for cycle in range(1, 241):
        crt += get_crt_pixel(cycle, values_during)
        if cycle % 40 == 0:
            crt += "\n"
    return crt


def execute_instructions(puzzle) -> list[int]:
    values_during = []
    X = 1

    for instruction in puzzle:

        if instruction.startswith("noop"):
            values_during.append(X)

        else:
            assert instruction.startswith("addx")
            values_during.append(X)
            values_during.append(X)
            delta = int(instruction.split()[1])
            X += delta

    values_during.append(X)
    return values_during


def extract_interesting_signal_strenghts(values_during) -> int:
    return sum(cycle * value_X_during_cycle(cycle, values_during) for cycle in range(20, 221, 40))


def value_X_during_cycle(cycle, values_during) -> int:
    # index 0 = X during cycle 1
    # index 1 = X after cycle 1 and during cycle 2
    return values_during[cycle - 1]


def get_crt_pixel(cycle, values_during) -> str:
    x_beam = (cycle - 1) % 40
    x_sprite = value_X_during_cycle(cycle, values_during)
    return "#" if abs(x_beam - x_sprite) <= 1 else "."


if __name__ == "__main__":
    main()
