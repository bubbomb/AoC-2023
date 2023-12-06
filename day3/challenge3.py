import re
import os

def get_line_sum(sum_line, next_line='', prev_line=''):
    total_value = 0
    i = 0

    while i < len(sum_line):
        if sum_line[i].isdigit():
            
            full_number, length_of_number = get_first_number_and_length(sum_line[i:])

            if is_part(i, length_of_number, sum_line, prev_line, next_line):
                total_value += full_number

            i += length_of_number
        else:
            i +=1

    return total_value

def has_any_symbol(line):
    return re.search(r'[!@#$%^&*()_+/=-]', line)

def is_part(index, length_of_number, line, prev_line, next_line):

    adjacent_start_index = max(0, index-1)
    adjacent_end_index = min(index +length_of_number + 1, len(line))

    adjacent_prev_line = prev_line[adjacent_start_index:adjacent_end_index]
    adjacent_sum_line = line[adjacent_start_index:adjacent_end_index]
    adjacent_next_line = next_line[adjacent_start_index:adjacent_end_index]

    return has_any_symbol(adjacent_prev_line + adjacent_sum_line + adjacent_next_line)


def get_first_number_and_length(line):
    match = re.search(r'\d+', line)
    return int(match.group()), match.end()

def get_total_gear_ratio(sum_line, next_line='', prev_line=''):
    total_gear_ratio = 0
    stars_indices = []

    for match in re.finditer(r'[*]', sum_line):
        stars_indices.append(match.start())

    for star_index in stars_indices:
        numbers = get_adjacent_numbers(star_index, prev_line, sum_line, next_line)
        if len(numbers) == 2:
            total_gear_ratio += numbers[0] * numbers[1]

    return total_gear_ratio

def get_adjacent_numbers(star_index, line1, line2, line3):
    adjacent_numbers = []
    adjacent_start_index = max(0, star_index - 1)
    adjacent_end_index = min(star_index + 1, len(line1))

    adjacent_numbers += get_numbers_in_range(line1, adjacent_start_index, adjacent_end_index)
    adjacent_numbers += get_numbers_in_range(line2, adjacent_start_index, adjacent_end_index)
    adjacent_numbers += get_numbers_in_range(line3, adjacent_start_index, adjacent_end_index)

    return adjacent_numbers

def get_numbers_in_range(line, left_index, right_index):
    numbers = []
    for match in re.finditer(r'\d+', line):
        if any_part_is_adjacent(match.start(), match.end()-1, left_index, right_index):
            numbers += [int(match.group())]
    return numbers

def any_part_is_adjacent(start, end, left_index, right_index):
        if left_index <= end <= right_index:
            return True
        elif left_index <= start <= right_index:
            return True

        return False

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
    first_puzzle_value = 0
    second_puzzle_value = 0
    prev_line = ''
    for i, line in enumerate(lines):
        if i > 0:
            prev_line = lines[i-1] 

        if i < len(lines)-1:
            next_line = lines[i+1]
        else:
            next_line = ''

        first_puzzle_value += get_line_sum(line, prev_line=prev_line, next_line=next_line)
        second_puzzle_value += get_total_gear_ratio(line, prev_line=prev_line, next_line=next_line)
    
    print('first_puzzle:', first_puzzle_value)
    print('second_puzzle:', second_puzzle_value)
