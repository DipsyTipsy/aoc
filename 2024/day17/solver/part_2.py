from solver import utils
from collections import defaultdict
import math

def combo(operand, registers):
    combo_operand = [
        0,
        1,
        2,
        3,
        registers["A"],
        registers["B"],
        registers["C"],
        None
    ]
    return combo_operand[operand]

def adv(operand, registers):
    A = int(registers["A"] / pow(2, combo(operand, registers)))
    #print(A, registers["A"], pow(2, combo(operand, registers)), combo(operand, registers))
    registers["A"] = A
    return None

def bxl(operand, registers):
    registers["B"] = registers["B"] ^ operand
    return None

def bst(operand, registers):
    registers["B"] = combo(operand, registers) % 8
    return None

def jnz(operand, registers):
    if registers["A"] == 0:
        return None
    return operand

def bxc(operand, registers):
    registers["B"] = registers["B"] ^ registers["C"]
    return None

def out(operand, registers):
    registers["output"] += str(combo(operand, registers)%8) + ","
    return None

def bdv(operand, registers):
    A = int(registers["A"] / pow(2, combo(operand, registers)))
    registers["B"] = A
    return None

def cdv(operand, registers):
    A = int(registers["A"] / pow(2, combo(operand, registers)))
    registers["C"] = A
    return None

def run_program(program, instructions, registers, desired_result):
    pointer = 0
    steps = 0
    registers["output"] = ""

    while pointer in range(len(program)):
        opcode = program[pointer]
        operand = program[pointer+1]
        #print("pointer:", pointer, "opcode",opcode, "operand",operand, instructions[opcode], registers)
        rcode = instructions[opcode](operand, registers)
        if rcode != None:
            pointer = rcode
        else:
            pointer += 2
        steps +=1
        if len(registers["output"]) > 0:
            if not desired_result.startswith(registers["output"][:-1]):
                print("- UNDESIRED, BREAKING", registers["output"], desired_result)
                return (len(registers["output"][:-1]), registers["output"][:-1])
                
    #print(pointer, registers)
    result = registers["output"][:-1]
    #print(result)
    return (len(result), result)


def solve(input_file: str):
    lines = utils.read_lines(input_file)
    registers = {"output": ""}
    program = []
    instructions = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]
    for line in lines:
        if line != "":
            key, value = line.split(":")
            print(key,value)
            match key:
                case "Register A":
                    registers["A"] = int(value)
                case "Register B":
                    registers["B"] = int(value)
                case "Register C":
                    registers["C"] = int(value)
                case "Program":
                    program = [int(x) for x in value.split(",")]
    
    print(registers, program)
    desired_result = ",".join([str(x) for x in program])
    checked =0
    num_correct = defaultdict(list)
    current_number = 1
    #skipping_order = [ 8192, 5777, 8, 1120, 1024, 263, 761, 984, 40, 1024, 1024, 1024, 984, 8, 32, 2311, 8192]
    #skipping_order = [ 278528+17825792+1158676480+75313971200+2506448961536000, 278528+17825792+1158676480+75313971200+2506448961536000]
    #skipping_order = [ 278528+17825792+1158676480, 278528+17825792+1158676480]
    #skipping_order = [ 38560753254400, 38560753254400]
    skipping_order = [8, 8, 8, 8, 8, 8, 8, 73, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 775]
    skipping_order = [8,8,8,8,8,8,8,8136,8,8,8,8,8,8,8,1040328,8,8,8,8,8,8,8,1048520]
    # 20 loop
    skipping_order = [8,8,8,8,8,8,8,536870856,8,8,8,8,8,8,8,536870856,8,8,8,8,8,8,8,536870856,8,8,8,8,8,8,8,536870856,8,8,8,8,8,8,8,536870856,8,8,8,8,8,8,8,536870856,8,8,8,8,8,8,8,536870856,8,8,8,8,8,8,8,536870856,8,8,8,8,8,8,8,536870856,8,8,8,8,8,8,8,536870856,8,8,8,8,8,8,8,536870856,8,8,8,8,8,8,8,536870856,8,8,8,8,8,8,8,536870856,8,8,8,8,8,8,8,536870856,8,8,8,8,8,8,8,1073741768]
    # 25 loop
    #skipping_order = [8,8,8,8,8,8,8,1099511627720]
    # 27 loop:
    skipping_order = [8,8,8,8,8,8,8,4398046511048,8,8,8,8,8,8,8,4398046511048,8,8,8,8,8,8,8,8796093022152,8,8,8,8,8,8,8,4398046511048,8,8,8,8,8,8,8,4398046511048,8,8,8,8,8,8,8,4398046511048,8,8,8,8,8,8,8,4398046511048,8,8,8,8,8,8,8,4398046511048,8,8,8,8,8,8,8,4398046511048,8,8,8,8,8,8,8,8796093022152,8,8,8,8,8,8,8,4398046511048,8,8,8,8,8,8,8,4398046511048,8,8,8,8,8,8,8,4398046511048,8,8,8,8,8,8,8,4398046511048]

    #skipping_order = [ 1602989851930985986, 1602989851930985986]
    #current_number = 48667096145872386

    #current_number = 771604085305975965186
    #current_number = 389058778729219586

    #29 starting point?
    current_number = 339431089290806786
    current_number = 339431089290806786 + 480 + 1048064 + 535822336 + 93415538688 + 8702140612608
    current_number = 288281808366667234
    skipping_order = skipping_order[::-1]

    #current_number = 1602989851930985986 #2,4,1,4,7,5,4,1,1,4,5,5,0,3,3,1
    #current_number = 20883327918377731586 #dead end?
    #current_number = 1602989851933185985
    seen_programs = defaultdict(list)
    orig_current_number = current_number
    for i in range(0, 10000000):
        #if (i % 8 == program[0]):
        registers["A"] = current_number 
        print(i, current_number, end = " ")
        result = run_program(program, instructions, registers, desired_result)

        #if result[1] == desired_result:
        #    print("Found", current_number)
        #    break
        if int(result[0]) > 2: 
            num_correct[int(result[0])].append(current_number)
            if int(result[0]) == 31:
                seen_programs[result[1]].append(current_number)
        checked +=1
        current_number = current_number - skipping_order[i%len(skipping_order)]
        if current_number < 0:
            break
        #current_number += 8


    for key, val in sorted(num_correct.items()):
        print(len(val),":", key, "/", len(desired_result))
        print(val[:12])
        print("Deltas: ", end="")
        deltas = defaultdict(int)
        cur = val[0]
        deltas["offset"] = cur - orig_current_number
        for x in val[1:]:
            delta = x - cur
            print(delta, end=" ")
            deltas[delta] += 1
            cur = x
        print()
        print(deltas)

        print()

    print(desired_result==result, desired_result, result, checked)
    for prog, indexes in seen_programs.items():
        print(prog, indexes[:10])

    
    return current_number
    