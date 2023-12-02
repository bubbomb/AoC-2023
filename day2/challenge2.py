import os

CUBES_IN_BAG = {
    'red': 12,
    'blue': 14,
    'green': 13,
}

def is_valid_game(draws):
    cube_draws = draws.split(';')
    for cube_draw in cube_draws:
        for cubes_by_color in cube_draw.split(','):
            cubes_by_color = cubes_by_color.strip()

            cube_color = cubes_by_color.split(' ')[1]
            number_of_cubes_drawn_of_color = int(cubes_by_color.split(' ')[0])

            total_cubes_in_bag_of_color = CUBES_IN_BAG.get(cube_color, 0)
            if total_cubes_in_bag_of_color < number_of_cubes_drawn_of_color:
                return False
    return True


def get_required_cubes(draws_string):
    required_cubes = {
        'red':0,
        'green':0,
        'blue':0,
    }

    for draw in draws_string.split(';'):
        for cubes_by_color in draw.split(','):
            cubes_by_color = cubes_by_color.strip()
            cube_color = cubes_by_color.split(' ')[1]
            number_of_cubes_drawn_of_color = int(cubes_by_color.split(' ')[0])
            if required_cubes[cube_color] < number_of_cubes_drawn_of_color:
                required_cubes[cube_color] = number_of_cubes_drawn_of_color
    
    return required_cubes

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
    for line in lines:
        draws_string = line.split(':')[1]
        game_number = int(line.split(':')[0].split(' ')[1])
        if is_valid_game(draws_string):
            first_puzzle_value += game_number

        required_cubes = get_required_cubes(draws_string)
        cubes_power = required_cubes['red'] * required_cubes['green'] * required_cubes['blue']
        second_puzzle_value += cubes_power
        
    print('first puzzle:', first_puzzle_value)
    print('second puzzle:', second_puzzle_value)
