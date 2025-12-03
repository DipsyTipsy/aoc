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
        max_idx = len(line)-12
        print(line)
        cur_line = line[:-12]
        for i in range(12):
            p_idx, a = find_max(cur_line)
            print(cur_line, a, p_idx, min_idx, max_idx)
            result += str(a)
            if i == 10:
                cur_line = line[min_idx:]
            else:
                min_idx = min_idx + p_idx + 1
                max_idx = len(line)-12+(i+2)
                cur_line = line[min_idx:max_idx]

        total += int(result)
        print(result)
        print()
    return total
        