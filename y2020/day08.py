def get_input():
    with open("inputs/08.txt") as f:
        return [line.strip() for line in f]


def main():
    puzzle = get_input()
    print("Part1:", part1(puzzle))
    # print("Part2:", part2(puzzle))


def part1(puzzle):
    instructions = [line.split() for line in puzzle]

    acc = 0
    visited = []

    cur = 0
    while True:
        acc_before = acc
        acc, cur = process_instruction(instructions, cur, acc)
        if cur in visited:
            return acc_before

        visited.append(cur)


def process_instruction(
    instructions: list[tuple[str, str]], current_line: int, acc: int
) -> tuple[int, int]:
    instruction, amount = instructions[current_line]

    if instruction == "nop":
        return acc, current_line + 1
    elif instruction == "acc":
        return acc + int(amount), current_line + 1
    elif instruction == "jmp":
        return acc, current_line + int(amount)

    raise ValueError


if __name__ == "__main__":
    main()
