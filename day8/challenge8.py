import os

def get_steps_to_z(text):
    directions, node_data = extract_data(text)
    print(directions)
    print(node_data)
    steps = 0

    current_location = 'AAA'
    found_zzz = False
    while not found_zzz:
        for step in directions:
            print(steps)
            print(current_location)
            if current_location == 'ZZZ':
                found_zzz = True
                break
            else:
                current_location = node_data[current_location][step]
                steps += 1

    return steps

def extract_data(text):
    directions, nodes = text.split('\n\n')
    data = {}
    for line in nodes.split('\n'):
        key, left_and_right = line.split('=')
        left, right = left_and_right.split(',')
        left = left.replace('(', '')
        right = right.replace(')', '')
        data[key.strip()] = {
            'L': left.strip(),
            'R': right.strip(),
        }

    return directions.strip(), data

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
    first_puzzle_value = get_steps_to_z(text)
    # second_puzzle_value = get_total_winnings(text, rank_map=CARD_RANK_MAP_JOKERS)

    print('first puzzle: ', first_puzzle_value)
    # print('second puzzle: ', second_puzzle_value)