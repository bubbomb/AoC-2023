import re
import os

def get_lowest_location(text):
    data = extract_data(text)
    ordered_maps = [
        data['seed-to-soil map'],
        data['soil-to-fertilizer map'],
        data['fertilizer-to-water map'],
        data['water-to-light map'],
        data['light-to-temperature map'],
        data['temperature-to-humidity map'],
        data['humidity-to-location map'],
    ]
    locations = []
    for seed in data['seeds']:
        print('seed: ', seed)
        locations += [get_location_from_seed(seed, ordered_maps)]

    return min(locations)


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
    first_puzzle_value = get_lowest_location(text)

    print('first puzzle: ', first_puzzle_value)