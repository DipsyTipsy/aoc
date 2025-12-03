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
        result = ""
        p_idx = 0
        min_idx = 0
        max_idx = len(line)-11
        cur_line = line[min_idx:max_idx]
        for i in range(1,13):
            p_idx, a = find_max(cur_line)
            result += str(a)

            min_idx = min_idx + p_idx + 1
            max_idx = len(line)-12+(i+1)
            cur_line = line[min_idx:max_idx]

        total += int(result)
    return total