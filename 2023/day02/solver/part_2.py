from solver import utils
import re


def solve(input_file: str):
    lines = utils.read_lines(input_file)

    contents = {"red": 12, "green": 13, "blue": 14}

    game_power = []
    for line in lines:
        game_id, games = tuple(line.split(":"))
        game_id = int(game_id.replace("Game ", ""))

        minimums = []
        for colour in contents:
            color_list = [int(x) for x in re.findall(f'(\d+) {colour}', line)]
            color_min = max(color_list)
            minimums.append(color_min)

        power = minimums[0]*minimums[1]*minimums[2]
        
        game_power.append(power)

    return sum(game_power)