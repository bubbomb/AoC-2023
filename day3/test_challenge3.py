from challenge3 import get_line_sum, get_total_gear_ratio

def test_get_line_sum_zero():
    line1 = '123.....'
    line2 = '123.....'
    line3 = '123.....'
    assert get_line_sum(line2, prev_line=line1, next_line=line3) == 0

def test_three_lines_zero():
    line1 = '467..114..'
    line2 = '...*......'
    line3 = '..35..633.'
    assert get_line_sum(line2, prev_line=line1, next_line=line3) == 0

def test_three_lines():
    line1 = '...*......'
    line2 = '..35..633.'
    line3 = '126*......'
    assert get_line_sum(line2, prev_line=line1, next_line=line3) == 35

def test_start_of_line():
    line1 = '...*......'
    line2 = '4.35..633.'
    line3 = '^26*......'
    assert get_line_sum(line2, prev_line=line1, next_line=line3) == 39

def test_end_of_line():
    line1 = '...*......'
    line2 = '4.35..63.7'
    line3 = '^26*.....$'
    assert get_line_sum(line2, prev_line=line1, next_line=line3) == 46

def test_start_lines():
    line1 = '4.16..63.7'
    line2 = '...*......'
    assert get_line_sum(line1, next_line=line2) == 16

def test_end_lines():
    line1 = '...$.*....'
    line2 = '..64.5.8..'
    assert get_line_sum(line2, prev_line=line1) == 69

def test_get_total_gear_ratio_zero():
    line1 = '123.....'
    line2 = '123.....'
    line3 = '123.....'
    assert get_total_gear_ratio(line2, prev_line=line1, next_line=line3) == 0

def test_get_total_gear_ratio():
    line1 = '467..114..'
    line2 = '...*......'
    line3 = '..35..633.'
    assert get_total_gear_ratio(line2, prev_line=line1, next_line=line3) == 467*35

def test_get_total_gear_ratio_zero_matches_with_star():
    line1 = '4....114..'
    line2 = '...*......'
    line3 = '......633.'
    assert get_total_gear_ratio(line2, prev_line=line1, next_line=line3) == 0

def test_get_total_gear_ratio_one_match_with_star():
    line1 = '4....114..'
    line2 = '..2*......'
    line3 = '......633.'
    assert get_total_gear_ratio(line2, prev_line=line1, next_line=line3) == 0

def test_get_total_gear_ratio_surround_star():
    line1 = '4....114..'
    line2 = '..2*2.....'
    line3 = '......633.'
    assert get_total_gear_ratio(line2, prev_line=line1, next_line=line3) == 4

def test_get_total_gear_ratio_star_at_beginning():
    line1 = '4....114..'
    line2 = '*.2.2.....'
    line3 = '3.....633.'
    assert get_total_gear_ratio(line2, prev_line=line1, next_line=line3) == 12

def test_get_total_gear_ratio_multi_star():
    line1 = '4......4..'
    line2 = '*.2.2..*..'
    line3 = '3......3..'
    assert get_total_gear_ratio(line2, prev_line=line1, next_line=line3) == 12 + 12

def test_get_total_gear_ratio_same_line():
    line1 = '4.........'
    line2 = '..2.5...*.'
    line3 = '3......2.5'
    assert get_total_gear_ratio(line2, prev_line=line1, next_line=line3) == 10

def test_get_total_gear_ratio_middle_and_corner():
    line1 = '4.........'
    line2 = '..2.5555*.'
    line3 = '3........1'
    assert get_total_gear_ratio(line2, prev_line=line1, next_line=line3) == 5555

def test_get_total_gear_ratio_three_directly_under():
    line1 = '4.........'
    line2 = '..2*.555..'
    line3 = '3.111....1'
    assert get_total_gear_ratio(line2, prev_line=line1, next_line=line3) == 222

def test_get_total_gear_ratio_missing_case():
    line1 = '......755.'
    line2 = '...$.*....'
    line3 = '.664.598..'
    assert get_total_gear_ratio(line2, prev_line=line1, next_line=line3) ==598*755