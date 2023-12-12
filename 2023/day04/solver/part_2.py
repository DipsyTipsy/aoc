from solver import utils
import math, re


def solve(input_file: str):
    # Each line is a game, need to offset
    lines = [re.sub(r'Card\s+\d+: ', "",x).split("|") for x in utils.read_lines(input_file)]

    game_cards = [1 for x in range(len(lines))]

    for i, line in enumerate(lines):
        winning_numbers = set([int(x) for x in line[1].split()])
        game_numbers = [int(x) in winning_numbers for x in line[0].split()]

        expansion_range = range(i+1, min(i+1+sum(game_numbers), len(game_cards)))

        for x in expansion_range:
            game_cards[x] += game_cards[i]

    return sum(game_cards)