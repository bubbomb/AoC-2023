from challenge5 import get_lowest_location_single_seed , extract_data, get_next_mapped_value, \
    get_lowest_location_seed_range, reverse_lookup_lowest_location_seed_range, get_prev_mapped_value

TEST_INPUT='''
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
'''.strip()

SMALL_TEST_INPUT='''
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48
'''.strip()

def test_big_input_challenge_1():
    assert get_lowest_location_single_seed(TEST_INPUT) == 35

def test_extract_data():
    assert extract_data(SMALL_TEST_INPUT) == {
        'seeds': [79, 14 , 55, 13],
        'seed-to-soil map': [
            {'destination_range_start': 50, 'source_range_start': 98, 'range_length':2, 'diff': -48, 'source_range_end': 100},
            {'destination_range_start': 52, 'source_range_start': 50, 'range_length':48, 'diff': 2, 'source_range_end': 98},
        ],
    }

def test_get_next_mapped_value():
    map = [
        {'destination_range_start': 50, 'source_range_start': 98, 'range_length':2, 'diff': -48, 'source_range_end': 100},
        {'destination_range_start': 52, 'source_range_start': 50, 'range_length':48, 'diff': 2, 'source_range_end': 98},
    ]
    assert get_next_mapped_value(79, map) == 81
    assert get_next_mapped_value(98, map) == 50
    assert get_next_mapped_value(14, map) == 14
    assert get_next_mapped_value(55, map) == 57
    assert get_next_mapped_value(13, map) == 13
    assert get_next_mapped_value(97, map) == 99
    assert get_next_mapped_value(49, map) == 49
    assert get_next_mapped_value(50, map) == 52

def test_big_input_challenge_2():
    assert get_lowest_location_seed_range(TEST_INPUT) == 46

def test_reverse_lookup_challenge_2():
    assert reverse_lookup_lowest_location_seed_range(TEST_INPUT) == 46

def test_get_prev_mapped_value():
    map = [
        {'destination_range_start': 50, 'source_range_start': 98, 'range_length':2, 'diff': -48, 'source_range_end': 100},
        {'destination_range_start': 52, 'source_range_start': 50, 'range_length':48, 'diff': 2, 'source_range_end': 98},
    ]
    assert get_prev_mapped_value(0, map) == 0
    assert get_prev_mapped_value(81, map) == 79
    assert get_prev_mapped_value(50, map) == 98
    assert get_prev_mapped_value(14, map) == 14
    assert get_prev_mapped_value(52, map) == 50
    assert get_prev_mapped_value(49, map) == 49
