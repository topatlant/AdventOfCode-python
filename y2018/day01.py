def get_input():
    with open("inputs/01.txt") as f:
        return f.read()


def part1(puzzle):
    return sum(int(x) for x in puzzle.splitlines())


def part2(puzzle):
    def find_duplicate_frequency(start_freq):
        f = start_freq
        for line in puzzle.splitlines():
            f += int(line)
            if f in frequencies:
                return True, f
            else:
                frequencies.add(f)

        # consumed whole list without reaching a duplicate
        return False, f

    current_freq = 0
    frequencies = {0}

    # todo ensure termination
    while True:
        found, freq = find_duplicate_frequency(current_freq)
        if found:
            return freq
        else:
            current_freq = freq


if __name__ == "__main__":
    print("Part 1:", part1(get_input()))
    print("Part 2:", part2(get_input()))
