from challenge3 import get_line_sum

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