from solver import utils

def check_valid(num):
    length = len(str(num))
    if len(str(num)) % 2 == 0:
        a = str(num)[:int(length/2)]
        b = str(num)[int(length/2):]
        return a  == b

    return False

def solve(input_file: str):
    lines = utils.read_lines(input_file)
    ranges = [(int(x.split("-")[0]), int(x.split("-")[1])) for x in lines[0].split(",")]
    invalid = []

    for min,max in ranges:

        for i in range(min, max+1):
            if check_valid(i):
                # print("invalid", i)
                invalid.append(i)
    
    return sum(invalid)


