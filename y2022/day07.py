from pathlib import PurePath
from typing import Iterator


def get_input():
    with open("inputs/07.txt") as f:
        return f.read().splitlines()


def main():
    puzzle = get_input()
    print("Part 1:", part1(puzzle))
    print("Part 2:", part2(puzzle))


def part1(puzzle: list[str]) -> int:
    all_dirs = populate_dirs(puzzle)
    return sum(
        x for x in (d.get_total_size() for d in all_dirs.values()) if x <= 100000
    )


def part2(puzzle: list[str]) -> int:
    all_dirs = populate_dirs(puzzle)
    total_cap = int(70e6)
    space_needed = int(30e6)
    total_used = all_dirs[str(PurePath("/"))].get_total_size()

    space_free = total_cap - total_used
    space_still_needed = space_needed - space_free

    return min(
        x
        for x in (d.get_total_size() for d in all_dirs.values())
        if x >= space_still_needed
    )


class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    @staticmethod
    def from_line(line: str) -> "File":
        size, name = line.split()
        return File(name, int(size))


class Directory:
    def __init__(self, name: str, files: list[File]):
        self.name = name
        self.files = files
        self.subdirs = []

    @staticmethod
    def from_ls_output(name: str, ls: list[str]) -> "Directory":
        files = [File.from_line(line) for line in ls if not line.startswith("dir")]
        # we do not track subdirs here, they will be added at the "ls" command
        return Directory(name, files)

    def add_subdir(self, sd: "Directory"):
        self.subdirs.append(sd)

    def get_total_size(self) -> int:
        return sum(f.size for f in self.files) + sum(
            d.get_total_size() for d in self.subdirs
        )


def populate_dirs(puzzle: list[str]) -> dict[str, Directory]:
    all_dirs = {}
    cur_dir = PurePath("/")

    commands = split_by_dollars(puzzle)

    for command, output in commands:

        if command.startswith("$ cd"):
            if command == "$ cd ..":
                cur_dir = cur_dir.parent
            else:
                cur_dir = cur_dir / (command.split()[-1])

        elif command.startswith("$ ls"):
            d = Directory.from_ls_output(cur_dir.name, output)
            all_dirs[str(cur_dir)] = d

            if cur_dir != PurePath("/"):
                # don't add root path to itself
                all_dirs[str(cur_dir.parent)].add_subdir(d)

        else:
            raise ValueError("Invalid terminal command")

    return all_dirs


def split_by_dollars(lines: list[str]) -> Iterator[tuple[str, list[str]]]:
    acc = [lines[0]]
    for line in lines[1:]:
        if line.startswith("$"):
            yield acc[0], acc[1:]
            acc = []
        acc.append(line)
    yield acc[0], acc[1:]


if __name__ == "__main__":
    main()
