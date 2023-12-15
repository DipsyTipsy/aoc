from solver import utils


def HASH(step):
    current_value = 0
    for chr in step:
        current_value += ord(chr)
        current_value = current_value * 17
        current_value = current_value % 256
    return current_value

def solve(input_file: str):
    lines = utils.read_lines(input_file)[0].split(",")
    print()

    sums = []
    for step in lines:
        sums.append(HASH(step))
    
    return sum(sums)
