from challenge7 import get_total_winnings, rank_hand, \
    HIGH_CARD, ONE_PAIR, TWO_PAIR, THREE_OF_A_KIND, FULL_HOUSE, FOUR_OF_A_KIND, FIVE_OF_A_KIND, \
    CARD_RANK_MAP_JOKERS

TEST_INPUT = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".strip()


def test_get_total_winnings():
    assert get_total_winnings(TEST_INPUT) == 6440


def test_rank_hand():
    assert rank_hand([3,3,3,3,3]) == FIVE_OF_A_KIND
    assert rank_hand([3,3,3,10,3]) == FOUR_OF_A_KIND
    assert rank_hand([3,3,3,10,2]) == THREE_OF_A_KIND
    assert rank_hand([3,2,10,3,13]) == ONE_PAIR
    assert rank_hand([3,2,10,9,13]) == HIGH_CARD
    assert rank_hand([5,5,5,2,2]) == FULL_HOUSE
    assert rank_hand([5,5,2,2,2]) == FULL_HOUSE
    assert rank_hand([5,5,11,2,2]) == TWO_PAIR


def test_get_total_winnings_with_jokers():
    assert get_total_winnings(TEST_INPUT, rank_map=CARD_RANK_MAP_JOKERS) == 5905

def test_rank_hand_with_jokers():
    assert rank_hand([1,1,1,1,1]) == FIVE_OF_A_KIND
    assert rank_hand([2,2,2,2,1]) == FIVE_OF_A_KIND
    assert rank_hand([2,2,2,13,1]) == FOUR_OF_A_KIND
    assert rank_hand([2,2,13,13,1]) == FULL_HOUSE
    assert rank_hand([2,2,13,1,1]) == FOUR_OF_A_KIND
    assert rank_hand([2,5,13,1,1]) == THREE_OF_A_KIND
    assert rank_hand([2,5,13,9,1]) == ONE_PAIR
