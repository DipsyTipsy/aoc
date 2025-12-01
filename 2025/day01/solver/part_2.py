from solver import utils

def handle_exception(num):
    n_dial = num
    if n_dial > 99:
        n_dial = n_dial - 100
    elif n_dial < 0:
        n_dial = 99 + n_dial + 1
    
    return n_dial

def smart_solve(lines):
    dial = 50
    num_zero = 0
    for line in lines:
        dir = -1 if line[0] == "L" else 1
        num = int(line[1:])
        n_dial = dial + (dir*num)
        counter = 0
        print(line, dial)

        while not n_dial in range(0,100):
            n_dial = handle_exception(n_dial)
            print("- Passing Zero",counter, dial, "->", n_dial)
            if dial != 0 and n_dial != 0:
                print("-- Adding")
                counter +=1
            dial = n_dial
        
        print("- ", line, num,dial, "->", n_dial)
        dial = n_dial
        if(dial == 0):
            print("- dial is 0 Adding")
            counter += 1
        if counter > 0:
            print("- NUM ZERO", counter)
        num_zero += counter
    
    print(num_zero)
    return num_zero

def dumb_solve(lines):
    dial = 50
    num_zero = 0
    for line in lines:
        dir = -1 if line[0] == "L" else 1
        num = int(line[1:])
        counter = 0
        for i in range(num):
            dial = dial + (1*dir)
            if dial < 0:
                dial = 99
            elif dial > 99:
                dial = 0

            if dial == 0:
                print(num, dial)
                counter += 1

        print(line, dial, counter)
        num_zero += counter
    return num_zero

def solve(input_file: str):
    lines = utils.read_lines(input_file)

    
    smart_zero = smart_solve(lines)
    print(smart_zero)

    dumb_zero = dumb_solve(lines)
    print(dumb_zero)

    return dumb_zero