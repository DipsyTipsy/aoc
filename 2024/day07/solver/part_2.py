from solver import utils
from itertools import permutations
from multiprocessing import Pool, Array

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
#    print("Checking", target, data)
    if sum(data) == target:
    #    print("Valid, sum")
        return True
    elif mult(data) == target:
    #    print("Valid, mult")
        return True
    elif combine(data) == target:
    #    print("Valid, combine")
        return True

    while len(data) > 1:
        a = data.pop(0)
        b = data.pop(0)

        for operator in ["*", "+", "||"]:
            _data = data.copy()
            if operator == "+":
                _data.insert(0, sum([a,b]))
                res = process(target, _data)
                if res:
                    return True
            elif operator == "||":
                _data.insert(0, int(str(a) + str(b)))
                res = process(target, _data)
                if res:
                    return True
            else:
                _data.insert(0, a*b)
                res = process(target, _data)
                if res:
                    return True
            if res:
                return True
    return False

def init(queue_list):
    global mp_list
    mp_list = queue_list

def queue_process(_input):
    if process(_input[1], _input[2]):
        with mp_list.get_lock():
            mp_list[_input[0]] = _input[1]

def solve(input_file: str):
    lines = [x.split(":") for x in utils.read_lines(input_file)]
    
    valid = 0
    data = []
    mp_results = Array("L", len(lines))
    for i, line in enumerate(lines):
        target = int(line[0])
        numbers = [int(x) for x in line[1].split(" ")[1:]]


        print(target, numbers)
        data.append((i, target, numbers))

    with Pool(8, initializer=init, initargs=(mp_results,)) as pool:
        pool.map(queue_process, data)

    
    print(sum(mp_results[:]))
    
    return sum(mp_results[:])