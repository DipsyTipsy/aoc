from solver import utils
import re, math


def solve(input_file: str):
    lines = [re.sub(r"[A-z:]+", "", x).split() for x in utils.read_lines(input_file)]
    times = [int(x) for x in lines[0]]
    records = [int(x) for x in lines[1]]
    games = [0 for x in range(len(times))]

    for i in range(len(times)):
        for millis in range(times[i]):
            distance = millis * (times[i] - millis)
            if distance > records[i]:
                games[i] += 1

    print(times, records, games)
    return math.prod(games)
