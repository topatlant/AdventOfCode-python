from y2018.day02 import *


def test_part1():
    i = "abcdef"
    assert any_letter_n_times(i, 2) == 0
    assert any_letter_n_times(i, 3) == 0
    i = "bababc"
    assert any_letter_n_times(i, 2) == 1
    assert any_letter_n_times(i, 3) == 1
    i = "abbcde"
    assert any_letter_n_times(i, 2) == 1
    assert any_letter_n_times(i, 3) == 0

    i = "abcccd"
    assert any_letter_n_times(i, 2) == 0
    assert any_letter_n_times(i, 3) == 1
    i = "aabcdd"
    assert any_letter_n_times(i, 2) == 1
    assert any_letter_n_times(i, 3) == 0
    i = "abcdee"
    assert any_letter_n_times(i, 2) == 1
    assert any_letter_n_times(i, 3) == 0
    i = "ababab"
    assert any_letter_n_times(i, 2) == 0
    assert any_letter_n_times(i, 3) == 1


def test_part2():
    i = """abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz"""

    assert part2(i) == "fgij"
