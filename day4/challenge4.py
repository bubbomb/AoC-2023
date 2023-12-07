import re
import os

def get_total_points(card_input):
    total_value = 0
    for card_line in card_input:
        total_value += get_card_points_from_line(card_line)
        
    return total_value

def get_card_points_from_line(card_line):
    data = split_data(card_line)

    points = 0
    for number in data['card_numbers']:
        if number in data['winning_numbers']:
            if points == 0:
                points = 1
            else:
                points *= 2

    return points

def split_data(card_line):
    card_title, number_data = card_line.split(':', 1)
    card_numbers, winning_numbers = number_data.split('|', 1)

    card_number = int(re.search(r'\d+', card_title).group())

    card_numbers = [int(match) for match in re.findall(r'\d+', card_numbers)]
    winning_numbers = {int(match) for match in re.findall(r'\d+', winning_numbers)}
    return {
        'card_number': card_number,
        'card_numbers': card_numbers,
        'winning_numbers': winning_numbers,
    }

def multiply_scratchcards(card_input):
    scratchcards = []
    for i, card_line in enumerate(card_input):
        data = split_data(card_line)
        matches = 0
        for number in data['card_numbers']:
            if number in data['winning_numbers']:
                matches += 1

        scratchcards.append({'matches': matches, 'count': 1})
    
    for i, scratchcard in enumerate(scratchcards):
        for j in range(scratchcard['matches']):
            scratchcards[i+j+1]['count'] += scratchcard['count']


    total_scratchcards = 0
    for scratchcard in scratchcards:
        total_scratchcards += scratchcard['count']

    return total_scratchcards


if __name__ == "__main__":
    print('--------------------------Start-----------------------------')
    print()

    print('Reading file...')
    file_path = os.path.dirname(__file__) + '/input.txt'
    print(file_path)
    print()
    input_file = open(file_path)

    print('Reading lines in file...')
    lines = input_file.readlines()
    print(len(lines), 'lines')
    print()

    print('calculating puzzles...')
    first_puzzle_value = get_total_points(lines)
    second_puzzle_value = multiply_scratchcards(lines)
    print('first puzzle: ', first_puzzle_value)
    print('second puzzle: ', second_puzzle_value)





