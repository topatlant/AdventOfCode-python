def get_input():
    with open("inputs/05.txt") as f:
        return [x.splitlines() for x in f.read().split("\n\n")]


def main():
    initial_state, instructions = get_input()
    print("Part 1:", part1(initial_state, instructions))
    print("Part 2:", part2(initial_state, instructions))


def part1(initial_state: list[str], instructions: list[str]) -> str:
    stacks = parse_initial_state(initial_state)
    for i in instructions:
        perform_action(stacks, i)
    return top_of_each_stack(stacks)


def part2(initial_state: list[str], instructions: list[str]) -> str:
    stacks = parse_initial_state(initial_state)
    for i in instructions:
        perform_action2(stacks, i)
    return top_of_each_stack(stacks)


def parse_initial_state(initial_state: list[str]) -> list[list[str]]:
    n_stacks = int(initial_state[-1].split()[-1])
    stacks = []
    for i in range(n_stacks):
        stacks.append(get_col(i, initial_state))
    return stacks


def get_col(i: int, initial_state: list[str]) -> list[str]:
    stack = []

    for line in initial_state[:-1]:
        line = line + " " * (40 - len(line))  # padding for shorter lines
        letter = line[1 + i * 4]
        if letter != " ":
            stack.append(letter)

    stack.reverse()  # last element is top, first element is bottom of stack
    return stack


def top_of_each_stack(stacks: list[list[str]]) -> str:
    return "".join(s[-1] for s in stacks)


def perform_action(stacks: list[list[str]], action: str) -> None:
    assert action.startswith("move")
    _, qty, _, _from, _, to = action.split()
    qty = int(qty)
    _from = int(_from) - 1
    to = int(to) - 1

    # move one box at a time
    for i in range(qty):
        stacks[to].append(stacks[_from].pop(-1))
    return


def perform_action2(stacks: list[list[str]], action: str) -> None:
    assert action.startswith("move")
    _, qty, _, _from, _, to = action.split()
    qty = int(qty)
    _from = int(_from) - 1
    to = int(to) - 1

    # move qty boxes at once
    stacks[to].extend(stacks[_from][-qty:])
    stacks[_from] = stacks[_from][:-qty]
    return


if __name__ == "__main__":
    main()
