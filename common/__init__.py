from typing import Iterable, Iterator


def split_by_blanks(lines: Iterable[str]) -> Iterator[list[str]]:
    acc = []
    for line in lines:
        line = line.strip()
        if line:
            acc.append(line)
        else:
            yield acc
            acc = []
    if acc:
        yield acc


def sign(a):
    return 0 if a == 0 else (1 if a > 0 else -1)
