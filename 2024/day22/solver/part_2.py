from solver import utils
from collections import defaultdict


def solve(input_file: str):
    lines = [ int(x) for x in utils.read_lines(input_file)]

    results = []
    price_map = defaultdict(list)
    for num in lines:
        secret = num
        prices = [int(str(secret)[-1])]
        changes = [None]
        _price_map = {}

        for i in range(2000):
            secret = (secret ^ (secret * 64)) % 16777216
            secret = (secret ^ int(secret / 32)) % 16777216
            secret = (secret ^ (secret * 2048)) % 16777216
            price = int(str(secret)[-1])
            change = None
            prices.append(price)
            change = prices[-1] - prices[-2]
            changes.append(change)
            if i > 3:
                _changes = changes[-4:]
                if len(set(_changes)) > 3:
                    change_str = ",".join([str(x) for x in _changes])
                    if change_str not in _price_map:
                        _price_map[change_str] = price
                        price_map[change_str].append(price)

    greatest_total = 0
    for change, prices in price_map.items():
        if sum(prices) > greatest_total:
            print(change, prices)
            greatest_total = sum(prices)
    
    return greatest_total


