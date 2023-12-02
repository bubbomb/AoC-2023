import os

number_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
spelled_numbers = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def get_calibration_value(calibration_text, digits_only=False):
    calibration_text = calibration_text.lower()
    first_number = get_first_number(calibration_text, digits_only=digits_only)
    last_number = get_first_number(calibration_text[::-1], reversed=True, digits_only=digits_only)

    return int(first_number) * 10 + int(last_number)

def get_first_number(text, reversed=False, digits_only=False):
    for i, character in  enumerate(text):
        if character.isdigit():
            return character
        elif not digits_only:
            for j, spelled_number in enumerate(spelled_numbers):
                number_check = text[i:i+len(spelled_number)]
                if reversed and number_check == spelled_number[::-1]:
                        return j
                elif number_check == spelled_number:
                    return j

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
        value = get_calibration_value(line, digits_only=True)
        first_puzzle_value += value

    print("puzzle 1 value:", first_puzzle_value)

    print('calculating 2nd puzzle...')
    second_puzzle_value = 0
    for line in lines:
        value = get_calibration_value(line)
        second_puzzle_value += value

    print("puzzle 2 value:", second_puzzle_value)