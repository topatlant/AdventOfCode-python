import os
import numpy as np
from typing import Union, Iterator

MIN_SO_FAR: int  # I have to find a better way than this global variable
MAX_DEPTH = 800  # tune this so that maximum recursion depth is not exceeded - final solution will be below 800 ;)


# Yes, I know this solution is not optimal - I thought about e.g. doing the full A*
# but this is also quick enough to do the job ;)
# Does depth-first recursion with manhattan-distance to target as the priority metrics
# and remembers visited points with lowest step count until then.


def get_input():
    with open("inputs/12.txt") as f:
        return f.read().splitlines()


def main():
    puzzle = get_input()
    print("Part 1:", part1(puzzle))
    # we have to get the input again, since my clever setup algorithm is destroying it :P
    puzzle = get_input()
    print("Part 2:", part2(puzzle))


def part1(puzzle, pt2=False) -> int:
    # Since only the number of steps is needed, I am turning start and target around.
    # This makes it easier for part2
    # We will therefore allow a max *descending* of one per step, instead of ascending...

    global MIN_SO_FAR
    MIN_SO_FAR = 10000

    heights, start, target = parse(puzzle)
    start, target = target, start  # search from target to start
    path = np.zeros_like(heights, "i")
    already_seen = {}

    min_steps = step(heights, path, already_seen, current=start, target=target, pt2=pt2)

    print("done!")
    return min_steps


def part2(puzzle) -> int:
    return part1(puzzle, pt2=True)


def parse(puzzle: list[str]) -> tuple[np.array, tuple[int, int], tuple[int, int]]:
    """parse the puzzle destructively, i.e. replace start with "a" and target with "z" """
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
    pt2: bool,
) -> Union[int, bool]:
    global MIN_SO_FAR

    # remember the path that brought us here
    n_steps = path.max()
    path[current] = n_steps + 1

    # did we finish?
    if current == target or (pt2 and heights[current] == 1):
        if n_steps < MIN_SO_FAR:
            # os.system("cls")  # for Windows systems
            print(f"Found a path with {n_steps} steps!")
            # print(visualize_path(path))
            MIN_SO_FAR = n_steps
        return n_steps

    # stop if we already know a better path to here - or else update knowledge.
    # Additionally stop if we are about to exceed the default recursion depth of Python ;)
    # don't worry - there exist solutions smaller than this
    if (
        n_steps > MAX_DEPTH
        or n_steps > MIN_SO_FAR
        or (current in already_seen and already_seen[current] <= n_steps)
    ):
        return False

    already_seen[current] = n_steps

    # check all options from here, starting with steps that bring us closer to target
    n_steps_children = []
    next_to_check = sorted(
        allowed_positions(heights, path, current),
        key=lambda p: manhattan_distance(p, target),
    )
    for next_position in next_to_check:
        # we have to branch (copy the visited path) to be able to do recursion/backtracking/different pathes
        n_steps_children.append(
            step(heights, path.copy(), already_seen, next_position, target, pt2)
        )

    if not n_steps_children or all(x is False for x in n_steps_children):
        # no route to target from here
        return False

    return min(n for n in n_steps_children if n is not False)


def manhattan_distance(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def allowed_positions(
    heights: np.array, visited: np.array, current: tuple[int, int]
) -> Iterator[tuple[int, int]]:
    def check_height(p):
        # cannot *descend* more than one height per step since we are searching in opposite direction
        return heights[p] >= heights[current] - 1

    def check_circular(p):
        # do not visit the same spot twice
        return not visited[p]

    def check_boundary(p):
        # do not leave grid
        return 0 <= p[0] < heights.shape[0] and 0 <= p[1] < heights.shape[1]

    for delta in (-1, 1):
        # vertical step
        new = current[0] + delta, current[1]
        if check_boundary(new) and check_circular(new) and check_height(new):
            yield new
        # horizontal step
        new = current[0], current[1] + delta
        if check_boundary(new) and check_circular(new) and check_height(new):
            yield new


def visualize_path(path: np.array):
    res = ""
    for i in range(path.shape[0]):
        for j in range(path.shape[1]):
            res += "#" if path[i, j] else " "
        res += "\n"
    return res


if __name__ == "__main__":
    main()
