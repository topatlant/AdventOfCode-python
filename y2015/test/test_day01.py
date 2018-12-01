from y2015 import day01


def test_part1():
    assert day01.part1("()()") == 0
    assert day01.part1("(())") == 0
    assert day01.part1("(((") == 3
    assert day01.part1("(()(()(") == 3
    assert day01.part1("))(((((") == 3
    assert day01.part1("())") == -1
    assert day01.part1("))(") == -1
    assert day01.part1(")))") == -3
    assert day01.part1(")())())") == -3


def test_part2():
    assert day01.part2(")") == 1
    assert day01.part2("()())") == 5
