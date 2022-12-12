import numpy as np
from typing import Union, Iterator, Optional

MIN_SO_FAR = 10000  # just for printing


# Yes, I know this is not optimal - I thought about doing the full A*
# but this is also quick enough to do the job ;)
# does depth-first recursion with manhattan-distance to target as the priority metrics
# and remembers visited points with shortest known path until then


def get_input():
    with open("inputs/12.txt") as f:
        return f.read().splitlines()


def main():
    puzzle = get_input()
    print("Part 1:", part1(puzzle))
    # print("Part 2:", part2(instructions))


def part1(puzzle) -> int:
    heights, start, target = parse(puzzle)

    path = np.zeros_like(heights, "i")
    already_seen = {}

    min_steps = step(heights, path, already_seen, current=start, target=target)

    print("done!")
    return min_steps


def parse(puzzle: list[str]) -> tuple[np.array, tuple[int, int], tuple[int, int]]:
    def get_height(char: str):
        return ord(char) - 96

    puzzle, start, target = determine_start_target(puzzle)
    heights = np.array([list(map(get_height, list(line))) for line in puzzle])

    return heights, start, target


def determine_start_target(
    puzzle: list[str],
) -> tuple[list[str], tuple[int, int], tuple[int, int]]:
    puzzle, start = find_and_replace_position(puzzle, "S", "a")
    puzzle, target = find_and_replace_position(puzzle, "E", "z")
    return puzzle, start, target


def find_and_replace_position(
    puzzle: list[str], char1, char2
) -> tuple[list[str], tuple[int, int]]:
    """find location of char1 and replace with char2"""
    loc = 0, 0
    for i, line in enumerate(puzzle):
        if char1 in line:
            loc = (i, line.index(char1))
            puzzle[i] = puzzle[i].replace(char1, char2)
            break
    return puzzle, loc


def step(
    heights: np.array,
    path: np.array,
    already_seen: dict[tuple[int, int], int],
    current: tuple[int, int],
    target: tuple[int, int],
) -> Union[int, bool]:
    global MIN_SO_FAR

    n_steps = final_number_of_steps(path)

    # remember the path that brought us here
    path[current] = path.max() + 1

    # did we finish?
    if current == target:
        if n_steps < MIN_SO_FAR:
            print(f"Found a path with {n_steps} steps!")
            # print(visualize_path(path))
            MIN_SO_FAR = n_steps
        return n_steps

    # stop if we already know a better path to here - or update knowledge
    # or stop if we are about to exceed the default recursion depth of Python ;)
    # since there exist solutions smaller than this
    if n_steps > 800 or (current in already_seen and already_seen[current] <= n_steps):
        return False
    else:
        already_seen[current] = n_steps

    # check all options from here
    n_steps = []
    next_to_check = sorted(
        allowed_positions(heights, path, current),
        key=lambda p: manhattan_distance(p, target),
    )
    for next_position in next_to_check:
        # check directions closer to target first
        # we have to branch (copy the visited path) to be able to do recursion/backtracking/different pathes
        n_steps.append(step(heights, path.copy(), already_seen, next_position, target))

    if n_steps == [] or all(x is False for x in n_steps):
        # no route to target from here
        return False

    return min(n for n in n_steps if n is not False)


def manhattan_distance(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def allowed_positions(
    heights: np.array, visited: np.array, current: tuple[int, int]
) -> Iterator[tuple[int, int]]:
    def check_height(p):
        # cannot climb more than one height per step
        return heights[p] <= heights[current] + 1

    def check_circular(p):
        # do not visit the same spot twice
        return not visited[p]

    def check_boundary(p):
        return 0 <= p[0] < heights.shape[0] and 0 <= p[1] < heights.shape[1]

    for delta in (-1, 1):
        # horizontal step
        new = current[0] + delta, current[1]
        if check_boundary(new) and check_circular(new) and check_height(new):
            yield new
        # vertical step
        new = current[0], current[1] + delta
        if check_boundary(new) and check_circular(new) and check_height(new):
            yield new


def final_number_of_steps(visited: np.array) -> int:
    return visited.max()


if __name__ == "__main__":
    main()
