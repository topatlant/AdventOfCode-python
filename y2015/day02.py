def get_input():
    with open("inputs/02.txt") as f:
        return f.read()


def part1(puzzle):
    result = 0
    for present in puzzle.splitlines():
        l, w, h = (int(x) for x in present.split("x"))
        faces = (l * w, l * h, w * h)
        result += 2 * sum(faces) + min(faces)

    return result


def part2(puzzle):
    result = 0
    for present in puzzle.splitlines():
        sides = [int(x) for x in present.split("x")]
        sides.sort()
        length = 2 * (sides[0] + sides[1])
        volume = sides[0] * sides[1] * sides[2]
        result += length + volume

    return result


if __name__ == "__main__":
    print("Part 1:", part1(get_input()))
    print("Part 2:", part2(get_input()))
