from challenge1 import get_calibration_value

def test_on_ends():
    assert get_calibration_value('1abc2') == 12

def test_in_middle():
    assert get_calibration_value('pqr3stu8vwx') == 38

def test_multi_number():
    assert get_calibration_value('a1b2c3d4e5f') == 15

def test_single_number():
    assert get_calibration_value('treb7uchet') == 77

def test_spelled_words():
    assert get_calibration_value('aifbthreeiugb8') == 38

def test_spelled_words_close_together():
    assert get_calibration_value('eightwo') == 82

def test_spelled_words_close_together_two_one():
    assert get_calibration_value('twone') == 21