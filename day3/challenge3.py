import re

def get_line_sum(sum_line, next_line='', prev_line=''):

    total_value = 0
    i = 0

    while i < len(sum_line):
        # print(i)
        if sum_line[i].isdigit():
            match = re.search(r'\d+', sum_line[i:])
            # print(match)
            # print(match.group())
            # print(match.span())
            lengthOfNumberFound = match.span()[1]
            adjacent_start_index = max(0, i-1)
            # print(adjacent_start_index)
            adjacent_end_index = min(i +lengthOfNumberFound + 1, len(sum_line))

            adjacent_prev_line = prev_line[adjacent_start_index:adjacent_end_index]
            adjacent_sum_line = sum_line[adjacent_start_index:adjacent_end_index]
            adjacent_next_line = next_line[adjacent_start_index:adjacent_end_index]
            # print(adjacent_prev_line)
            # print(adjacent_sum_line)
            # print(adjacent_next_line)

            
            if has_symbol(adjacent_prev_line + adjacent_sum_line + adjacent_next_line):
                total_value += int(match.group())

            i += lengthOfNumberFound
        else:
            i +=1

    return total_value

def has_symbol(line):
    return re.search(r'[!@#$%^&*()_+]', line)

