from solver import utils
import re

def check_valid(num):
    num = str(num)
    for check in range(len(num)):
        r = re.sub(num[:check], "", num)
        if len(r) == 0:
            print(r, len(r))
            return True


    return False

def solve(input_file: str):
    lines = utils.read_lines(input_file)
    ranges = [(int(x.split("-")[0]), int(x.split("-")[1])) for x in lines[0].split(",")]
    invalid = []

    for min,max in ranges:
        print(min,max)

        for i in range(min, max+1):
            if check_valid(i):
                print("invalid", i)
                invalid.append(i)
    
    return sum(invalid)




