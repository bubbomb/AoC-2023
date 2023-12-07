import re
import os

MAP_ORDER = [
    'seed-to-soil map',
    'soil-to-fertilizer map',
    'fertilizer-to-water map',
    'water-to-light map',
    'light-to-temperature map',
    'temperature-to-humidity map',
    'humidity-to-location map',
]
def get_lowest_location_single_seed(text):
    data = extract_data(text)
    locations = []
    ordered_maps = [data[map_name] for map_name in MAP_ORDER]
    for seed in data['seeds']:
        print('seed: ', seed)
        locations += [get_location_from_seed(seed, ordered_maps)]

    return min(locations)

def get_lowest_location_seed_range(text):
    data = extract_data(text)
    ordered_maps = [data[map_name] for map_name in MAP_ORDER]

    seed_ranges = []
    for i, seed in enumerate(data['seeds']):
        if i % 2 == 0:
            seed_ranges += [
                {'range_start': seed, 'range_length':data['seeds'][i+1]}
            ]

    lowest_location = None
    for seed_range in seed_ranges:
        print('seed_range: ', seed_range)
        for i in range(seed_range['range_length']):
            seed = seed_range['range_start'] + i
            new_location = get_location_from_seed(seed, ordered_maps)
            if not lowest_location:
                lowest_location = new_location
                print('lowest_location: ', lowest_location)
                print('seed: ', seed)
            elif new_location < lowest_location:
                lowest_location = new_location
                print('lowest_location: ', lowest_location)
                print('seed: ', seed)

    return lowest_location


def extract_data(text):
    almanac_blocks = text.split('\n\n')
    data = {'seeds': get_numbers(almanac_blocks[0])}
    for block in almanac_blocks[1:]:
        name, map_data = block.split(':')
        data[name] = []
        for line in map_data.strip().split('\n'):
            map_numbers = get_numbers(line)
            data[name] += [{
                'destination_range_start': map_numbers[0],
                'source_range_start': map_numbers[1],
                'range_length': map_numbers[2],
            }]
    return data

def get_numbers(line):
    return [int(digit) for digit in re.findall(r'\d+', line)]

def get_next_mapped_value(original_value, map):
    for range in map:
        range_start = range['source_range_start']
        range_end = range_start + range['range_length']
        if range_start <= original_value <= range_end:
            diff = range['destination_range_start'] - range_start
            return original_value + diff
            
    return original_value

def get_location_from_seed(seed, ordered_maps):
    next_value = seed
    for map in ordered_maps:
        next_value = get_next_mapped_value(next_value, map)
    return next_value 

if __name__ == "__main__":
    print('--------------------------Start-----------------------------')
    print()

    print('Reading file...')
    file_path = os.path.dirname(__file__) + '/input.txt'
    print(file_path)
    print()
    input_file = open(file_path)

    print('Reading file...')
    text = input_file.read()
    print()

    print('calculating puzzles...')
    first_puzzle_value = get_lowest_location_single_seed(text)
    second_puzzle_value = get_lowest_location_seed_range(text)

    print('first puzzle: ', first_puzzle_value)
    print('second puzzle: ', second_puzzle_value)