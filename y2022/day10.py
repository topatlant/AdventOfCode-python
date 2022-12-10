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


def execute_instructions(puzzle: list[str]) -> list[int]:
    values_during = []
    x = 1

    for instruction in puzzle:

        if instruction.startswith("noop"):
            values_during.append(x)

        else:
            assert instruction.startswith("addx")
            values_during.append(x)
            values_during.append(x)
            delta = int(instruction.split()[1])
            x += delta

    values_during.append(x)
    return values_during


def extract_interesting_signal_strenghts(values_during: list[int]) -> int:
    return sum(
        cycle * value_x_during_cycle(cycle, values_during)
        for cycle in range(20, 221, 40)
    )


def value_x_during_cycle(cycle: int, values_during: list[int]) -> int:
    # index 0 = X during cycle 1
    # index 1 = X after cycle 1 and during cycle 2
    # ...
    return values_during[cycle - 1]


def get_crt_pixel(cycle: int, values_during: list[int]) -> str:
    x_beam = (cycle - 1) % 40
    x_sprite = value_x_during_cycle(cycle, values_during)
    return "#" if abs(x_beam - x_sprite) <= 1 else "."


if __name__ == "__main__":
    main()
