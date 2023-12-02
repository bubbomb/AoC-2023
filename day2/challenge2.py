import os

CUBES_IN_BAG = {
    'red': 12,
    'blue': 14,
    'green': 13,
}

def is_valid_game(cube_draws_in_entire_game):

    cube_draws = cube_draws_in_entire_game.split(';')
    for cube_draw in cube_draws:
        for cubes_by_color in cube_draw.split(','):
            cubes_by_color = cubes_by_color.strip()

            cube_color = cubes_by_color.split(' ')[1]
            number_of_cubes_drawn_of_color = int(cubes_by_color.split(' ')[0])

            total_cubes_in_bag_of_color = CUBES_IN_BAG.get(cube_color, 0)
            if total_cubes_in_bag_of_color < number_of_cubes_drawn_of_color:
                return False

    return True

def get_game_data(game_string):
    game_number = int(game_string.split(':')[0].split(' ')[1])
    draws_string = game_string.split(':')[1]
    draws_data = []
    for draw in draws_string.split(';'):
        draw_data = {}
        for cubes_by_color in draw.split(','):
            cubes_by_color = cubes_by_color.strip()
            cube_color = cubes_by_color.split(' ')[1]
            number_of_cubes_drawn_of_color = int(cubes_by_color.split(' ')[0])
            draw_data[cube_color] = number_of_cubes_drawn_of_color

        draws_data += [draw_data]
    
    return {
        'number': game_number,
        'draws':draws_data
    }



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

    print('calculating 1st puzzle...')
    first_puzzle_value = 0
    for line in lines:
        draws_string = line.split(':')[1]
        game_number = int(line.split(':')[0].split(' ')[1])
        if is_valid_game(draws_string):
            first_puzzle_value += game_number
        else:
            print('invalid game: ', game_number)

    print(first_puzzle_value)

