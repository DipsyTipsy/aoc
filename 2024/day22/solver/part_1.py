from solver import utils


def solve(input_file: str):
    lines = [ int(x) for x in utils.read_lines(input_file)]
    # print(lines)

    results = []
    for num in lines:
        secret = num
        for i in range(2000):
            secret = (secret ^ (secret * 64)) % 16777216
            secret = (secret ^ int(secret / 32)) % 16777216
            secret = (secret ^ (secret * 2048)) % 16777216
        results.append(secret)

    return sum(results)
