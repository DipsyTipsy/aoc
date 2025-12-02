from solver import utils

def check_valid(num):
    length = len(str(num))
    half = int(length/2)
    if not length % 2:
        a = str(num)[:half]
        b = str(num)[half:]
        return a  == b
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