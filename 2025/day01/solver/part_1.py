from solver import utils

def handle_exception(num):
    n_dial = num
    if n_dial > 99:
        n_dial = n_dial - 100
    elif n_dial < 0:
        n_dial = 99 + n_dial + 1
    
    return n_dial

def solve(input_file: str):
    lines = utils.read_lines(input_file)

    dial = 50
    num_zero = 0

    for line in lines:
        dir = -1 if line[0] == "L" else 1
        num = int(line[1:])
        n_dial = dial + (dir*num)

        while not n_dial in range(-1,100):
            n_dial = handle_exception(n_dial)
        
        print(line, num,dial, "->", n_dial)
        dial = n_dial
        if(dial == 0):
            num_zero += 1
    
    return num_zero
