from solver import utils

def check_valid(num):
    num = str(num)
    for check in range(1,int(len(num)/2)+1):
        if not len(num) % check:
            to_check = num[:check]
            r = num.replace(to_check, "")
            if len(r) == 0:
                return True
    return False

def solve(input_file: str):
    lines = utils.read_lines(input_file)
    ranges = [(int(x.split("-")[0]), int(x.split("-")[1])) for x in lines[0].split(",")]
    invalid = 0

    for min,max in ranges:
        for i in range(min, max+1):
            if check_valid(i):
                invalid += i
    
    return invalid