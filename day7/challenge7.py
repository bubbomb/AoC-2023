import os 

CARD_RANK_MAP = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
}

CARD_RANK_MAP_JOKERS = {
    **CARD_RANK_MAP,
    'J':1,
}

FIVE_OF_A_KIND = 7
FOUR_OF_A_KIND = 6
FULL_HOUSE = 5
THREE_OF_A_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH_CARD = 1

def get_total_winnings(text, rank_map=CARD_RANK_MAP):
    hands = extract_data(text, rank_map=rank_map)
    hands.sort(key=sort_by_rank)

    total_winnings = 0
    for i, hand in enumerate(hands):
        total_winnings += hand['bid'] * (i+1)
    return total_winnings


def sort_by_rank(hand):
    return (hand['rank'], hand['cards'])

def rank_hand(hand):
    card_counts = {}
    for card in hand:
        card_counts[card] = card_counts.get(card, 0) + 1

    joker_count = card_counts.get(1, 0)

    if card_counts.get(1, False):
        del card_counts[1]

    counts_of_same_card = list(card_counts.values())
    counts_of_same_card.sort(reverse=True)

    highest_count = joker_count
    if counts_of_same_card:
        highest_count += counts_of_same_card[0]

    if highest_count == 5:
        return FIVE_OF_A_KIND
    if highest_count == 4:
        return FOUR_OF_A_KIND
    if is_full_house(counts_of_same_card, joker_count):
        return FULL_HOUSE
    if counts_of_same_card == [2,2,1]:
        return TWO_PAIR
    if highest_count == 3:
        return THREE_OF_A_KIND
    if highest_count == 2:
        return ONE_PAIR
    return HIGH_CARD

def is_full_house(counts_of_same_card, jokers):
    if counts_of_same_card == [3,2]:
        return True
    elif counts_of_same_card == [2,2] and jokers == 1:
        return True
    return False

def extract_data(text, rank_map=CARD_RANK_MAP):
    lines = text.split('\n')

    hands = []
    for line in lines:
        halves = line.split()
        cards = halves[0]
        card_list = []
        for card in cards:
            if card.isdigit():
                card_list += [int(card)]
            else:
                card_list += [rank_map[card]]

        hands += [{
            'cards': card_list,
            'bid': int(halves[1]),
            'rank': rank_hand(card_list),
        }]
    return hands

if __name__ == "__main__":
    print('--------------------------Start-----------------------------')
    print()

    print('Opening file...')
    file_path = os.path.dirname(__file__) + '/input.txt'
    print(file_path)
    print()
    input_file = open(file_path)

    print('Reading file...')
    text = input_file.read()
    print()

    print('calculating puzzles...')
    first_puzzle_value = get_total_winnings(text)
    second_puzzle_value = get_total_winnings(text, rank_map=CARD_RANK_MAP_JOKERS)

    print('first puzzle: ', first_puzzle_value)
    print('second puzzle: ', second_puzzle_value)