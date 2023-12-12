from solver import utils
import re


def solve(input_file: str):
    lines = utils.read_lines(input_file)
    contents = {"red": 12, "green": 13, "blue": 14}

    game_ids = []
    for line in lines:
        game_id, games = tuple(line.split(":"))
        game_id = int(game_id.replace("Game ", ""))

        max_legal = True
        for colour, max_val in contents.items():
            color_list = [int(x) for x in re.findall(f'(\d+) {colour}', line)]
            color_max = max(color_list)
            if color_max > max_val:
                max_legal = False
                break
        
        if max_legal:
            game_ids.append(game_id)

    return sum(game_ids)

