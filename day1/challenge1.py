import os

def get_calibration_value(calibration_text):

    calibration_text = replace_spelled_numbers(calibration_text)

    number_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
    first_number = ''
    last_number = ''
    for character in calibration_text:
        if character in number_set:
            if first_number == '':
                first_number = character
            last_number = character

    return int(first_number + last_number)

def replace_spelled_numbers(calibration_text):
    spelled_numbers = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i, spelled_number in enumerate(spelled_numbers):
        index = calibration_text.find(spelled_number)
        if index >= 0:
            calibration_text = calibration_text[:index] + spelled_number[0] + str(i) + spelled_number[-1] + calibration_text[index:]

    for spelled_number in spelled_numbers:
        calibration_text = calibration_text.replace(spelled_number, '')

    return calibration_text


if __name__ == "__main__":
    print('--------------------------Start-----------------------------')
    print('')

    print('Reading file...')
    file_path = os.path.dirname(__file__) + '/input.txt'
    print(file_path)
    input_file = open(file_path)

    print('Reading lines in file...')
    lines = input_file.readlines()

    print('calculating...')
    total_value = 0
    for line in lines:
        total_value += get_calibration_value(line)
        print(total_value)
    