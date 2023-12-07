from challenge4 import get_total_points, get_card_points_from_line, multiply_scratchcards

TEST_INPUT = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""


def test_get_card_points_from_line():
    line = 'Card 1: 12  4  5 | 21  5 63  4'
    assert get_card_points_from_line(line) == 2

def test_get_card_points_from_line():
    line = 'Card 12: 12  4  5 | 21  5 63  4 12'
    assert get_card_points_from_line(line) == 4

def test_big_input():
    lines = [line for line in TEST_INPUT.strip().split('\n')]
    assert get_total_points(lines) == 13


def test_multiply_scratchcards():
    lines = [line for line in TEST_INPUT.strip().split('\n')]
    assert multiply_scratchcards(lines) == 30