from y2015.day05 import *


def test_part1():
    assert is_nice_part1("ugknbfddgicrmopn")
    assert is_nice_part1("aaa")
    assert not is_nice_part1("jchzalrnumimnmhp")
    assert not is_nice_part1("haegwjzuvuyypxyu")
    assert not is_nice_part1("dvszwmarrgswjxmb")


def test_part2():
    assert is_nice_part2("qjhvhtzxzqqjkmpb")
    assert is_nice_part2("xxyxx")
    assert not is_nice_part2("uurcxstgmygtbstg")
    assert not is_nice_part2("ieodomkazucvgmuy")
