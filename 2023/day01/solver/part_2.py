from solver import utils
import re


def solve(input_file: str):
    def find_num_occurance(line, iteration_modifier):
        current_word = ""
        for i in line[::iteration_modifier]:
            current_word += i
            
            if i.isdigit():
                return int(i)

            for word, numb in str_to_num.items():
                if word in current_word[::iteration_modifier]:
                    return numb


    lines = utils.read_lines(input_file)

    str_to_num = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

    numbs = []
    for line in lines:
        start_word = find_num_occurance(line, 1)
        end_word = find_num_occurance(line, -1)

        numbs.append(int(f"{start_word}{end_word}"))

    return sum(numbs)