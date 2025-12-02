from solver import utils

def check_valid(num):
    cnum = str(num)
    return num if cnum.replace(cnum[len(cnum) // 2:], "") == "" else 0

def solve(input_file: str):
    lines = utils.read_lines(input_file)[0].split(",")
    ranges = ((int(a) for a in x.split("-")) for x in lines)
    invalid = 0

    for min,max in ranges:
        invalid += sum((check_valid(x) for x in range(min, max+1)))
    return invalid