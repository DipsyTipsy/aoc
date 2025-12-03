from solver import utils

def find_max(line):
    ints = [int(x) for x in line]
    biggest = max(ints)
    idx = line.find(str(biggest))
    return (idx, biggest)

def solve(input_file: str):
    lines = utils.read_lines(input_file)
    total = 0
    for line in lines:
        result = 0
        a_idx, a = find_max(line[:-1])

        new_line = line[a_idx+1:]
        b_idx, b = find_max(new_line)

        total += int(str(a)+str(b))
    return total
        