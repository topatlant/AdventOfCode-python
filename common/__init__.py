from itertools import tee
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


def pairwise(iterable):
    """s -> (s0,s1), (s1,s2), (s2, s3), ..."""
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def triplewise(iterable):
    """Return overlapping triplets from an iterable"""
    # triplewise('ABCDEFG') -> ABC BCD CDE DEF EFG
    for (a, _), (b, c) in pairwise(pairwise(iterable)):
        yield a, b, c
