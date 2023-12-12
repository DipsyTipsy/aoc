from solver import utils
import re, math


def solve(input_file: str):
    lines = [re.sub(r"[A-z:\s]+", "", x) for x in utils.read_lines(input_file)]
    times = int(lines[0])
    records = int(lines[1])
    games = 0
    print(times, records, games)

    for millis in range(times):
        distance = millis * (times - millis)
        if distance > records:
            games += 1

    print(times, records, games)
    return games