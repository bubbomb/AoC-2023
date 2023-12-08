import re
import os

def get_number_of_winning_strategies(text):
    times, distances = get_times_and_distances(text)

    total_winning_strategies = 1
    for i, time in enumerate(times):
        first_winning_strategy = get_first_winning_strategy(time, distances[i])
        total_winning_strategies *= time - (2* first_winning_strategy) + 1

    return total_winning_strategies


def get_times_and_distances(text):
    lines = text.split('\n')
    times = [int(digit) for digit in re.findall(r'\d+', lines[0])]
    distances = [int(digit) for digit in re.findall(r'\d+', lines[1])]
    return times, distances

def get_first_winning_strategy(time_allowed, target_distance):

    for i in range(time_allowed):
        hold_milliseconds = i+1
        time_left = time_allowed - hold_milliseconds
        strategy_distance = time_left * hold_milliseconds
        if strategy_distance > target_distance:
            return hold_milliseconds

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
    first_puzzle_value = get_number_of_winning_strategies(text)
    # second_puzzle_value = reverse_lookup_lowest_location_seed_range(text)

    print('first puzzle: ', first_puzzle_value)
    # print('second puzzle: ', second_puzzle_value)