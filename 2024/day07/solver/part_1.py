from solver import utils
from itertools import permutations

def mult(data):
    result = 0
    for i in range(1, len(data)):
        result += data[i]*data[i-1]
    return result

def combine(data):
    result = "" 
    for i in range(1, len(data)):
        result += str(data[i]) + str(data[i-1])
    return result

def process(target, data):
    #print("Checking", target, data)
    if sum(data) == target:
        return True
    elif combine(data) == target:
        return True

    while len(data) > 1:
        a = data.pop(0)
        b = data.pop(0)

        for operator in ["*", "+"]:
            _data = data.copy()
            if operator == "+":
                _data.insert(0, sum([a,b]))
                res = process(target, _data)
                if res:
                    return True
            else:
                _data.insert(0, a*b)
                res = process(target, _data)
                if res:
                    return True

        return False


def solve(input_file: str):
    lines = [x.split(":") for x in utils.read_lines(input_file)]
    
    
    valid = 0
    for line in lines:
        target = int(line[0])
        numbers = [int(x) for x in line[1].split(" ")[1:]]


        print(target, numbers)
        if process(target, numbers):
            print("- Valid")
            valid += target
    
    return valid

