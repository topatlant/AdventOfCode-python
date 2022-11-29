def get_input():
    with open("inputs/03.txt") as f:
        return f.read()


def part1(puzzle):
    numbers = [i for i in puzzle.splitlines()]
    bitlength = len(numbers[0])
    gamma = ""
    epsilon = ""
    for b in range(bitlength):
        if find_most_common_bit(numbers, b):
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return int(gamma, 2) * int(epsilon, 2)


def part2(puzzle):
    numbers = [i for i in puzzle.splitlines()]

    oxygen_numbers = numbers
    bit = 0
    while len(oxygen_numbers) > 1:
        oxygen_numbers = filter_most_common_bit(oxygen_numbers, bit)
        bit += 1

    assert len(oxygen_numbers) == 1
    oxygen = int(oxygen_numbers[0], 2)

    co2_numbers = numbers
    bit = 0
    while len(co2_numbers) > 1:
        co2_numbers = filter_least_common_bit(co2_numbers, bit)
        bit += 1
    assert len(co2_numbers) == 1
    co2 = int(co2_numbers[0], 2)
    return oxygen * co2


def find_most_common_bit(numbers, bit):
    n_numbers = len(numbers)
    n_of_ones = sum(int(x[bit]) for x in numbers)
    return 1 if n_of_ones >= n_numbers / 2 else 0


def filter_most_common_bit(numbers, bit):
    mcb = str(find_most_common_bit(numbers, bit))
    return list(filter(lambda x: x[bit] == mcb, numbers))


def filter_least_common_bit(numbers, bit):
    mcb = str(find_most_common_bit(numbers, bit))
    return list(filter(lambda x: x[bit] != mcb, numbers))


if __name__ == "__main__":
    print("Part 1:", part1(get_input()))
    print("Part 2:", part2(get_input()))
