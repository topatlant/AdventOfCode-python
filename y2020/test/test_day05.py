from y2020.day05 import *


def test_get_row_col():
    assert extract_row_col("FBFBBFFRLR") == (44, 5)
    assert extract_row_col("BFFFBBFRRR") == (70, 7)
    assert extract_row_col("FFFBBBFRRR") == (14, 7)
    assert extract_row_col("BBFFBBFRLL") == (102, 4)


def test_get_seat_id():
    assert get_seat_id("FBFBBFFRLR") == 357
    assert get_seat_id("BFFFBBFRRR") == 567
    assert get_seat_id("FFFBBBFRRR") == 119
    assert get_seat_id("BBFFBBFRLL") == 820
