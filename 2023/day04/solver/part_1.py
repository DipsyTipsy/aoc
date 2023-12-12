from solver import utils
import math, re


def solve(input_file: str):
    lines = [re.sub(r'Card\s+\d+: ', "",x).split("|") for x in utils.read_lines(input_file)]

    winnings = []
    for line in lines:
        winning_numbers = set([int(x) for x in line[1].split()])
        game_numbers = [int(x) in winning_numbers for x in line[0].split()]

        current_game = 0
        for x in range(sum(game_numbers)):
            if x == 0:
                current_game +=1
            else:
                current_game = current_game*2

        winnings.append(current_game)

    return sum(winnings)

