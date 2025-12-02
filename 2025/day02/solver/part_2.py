from solver import utils

def check_valid(num):
    num = str(num)
    str_len = len(num)
    for check in range(1, (str_len // 2) + 1):
        if not str_len % check:
            to_check = num[:check]
            r = num.replace(to_check, "")
            if len(r) == 0:
                return int(num)
    return 0

def solve(input_file: str):
    lines = utils.read_lines(input_file)[0].split(",")
    ranges = ((int(a) for a in x.split("-")) for x in lines)
    invalid = 0

    for min,max in ranges:
        invalid += sum((check_valid(x) for x in range(min, max+1)))
    
    return invalid