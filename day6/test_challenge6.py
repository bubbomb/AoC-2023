from challenge6 import get_number_of_winning_strategies, get_first_winning_strategy

TEST_INPUT = """
Time:      7  15   30
Distance:  9  40  200
""".strip()


def test_challenge_1_from_input():
    assert get_number_of_winning_strategies(TEST_INPUT) == 288


def test_get_first_winning_strategy():
    assert get_first_winning_strategy(7,9) == 2
    assert get_first_winning_strategy(15,40) == 4
    assert get_first_winning_strategy(30,200) == 11