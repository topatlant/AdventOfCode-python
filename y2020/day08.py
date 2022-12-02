from copy import deepcopy


def get_input():
    with open("inputs/08.txt") as f:
        return [line.strip() for line in f]


def main():
    puzzle = get_input()
    print("Part1:", part1(puzzle))
    print("Part2:", part2(puzzle))


def part1(puzzle):
    instructions = [line.split() for line in puzzle]
    return get_acc_at_end(instructions)[1]


def part2(puzzle):
    instructions = [line.split() for line in puzzle]

    positions_to_change = [
        index
        for (index, instruction) in enumerate(instructions)
        if instruction[0] in ("jmp", "nop")
    ]

    for p in sorted(positions_to_change, reverse=True):
        changed_programm = swap_one_instruction(instructions, p)

        terminates, final_acc = get_acc_at_end(changed_programm)
        if terminates:
            print("Swapping instruction", p, "was successful")
            return final_acc


def get_acc_at_end(instructions: list[tuple[str, str]]) -> tuple[bool, int]:
    acc = 0
    acc_before: int
    cur = 0
    visited = []

    while cur < len(instructions):
        visited.append(cur)
        acc_before = acc

        acc, cur = process_instruction(instructions, cur, acc)

        if cur in visited:
            return False, acc_before  # program loops

    return True, acc  # program reaches the end


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


def swap_one_instruction(instructions, location):
    changed_program = deepcopy(instructions)
    if changed_program[location][0] == "jmp":
        changed_program[location][0] = "nop"
    elif changed_program[location][0] == "nop":
        changed_program[location][0] = "jmp"
    else:
        raise ValueError

    return changed_program


if __name__ == "__main__":
    main()
