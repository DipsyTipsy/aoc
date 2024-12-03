from solver import utils
import re


def solve(input_file: str):
    lines = str(utils.read_lines(input_file))
    print()
    data = lines.split("don't()")

    multiplications = []
    for i, d in enumerate(data):
        print(i,d)

        enabled = str(d.split("do()")[1:])
        if i == 0:
            enabled = d
        
        found = re.findall(r"mul\(\d+,\d+\)", enabled)
        for x in found:
            multiplications.append(x)
            print(found)

    print(multiplications)
    total = 0
    for d in multiplications:
        x, y  = d.replace("mul(", "").replace(")", "").split(",")
        total += int(x)*int(y)

    return total