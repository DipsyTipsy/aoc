from solver import utils

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
    print(f"- out: {combo(operand, registers)%8},")
    registers["output"].append(combo(operand, registers)%8)
    return None

def bdv(operand, registers):
    A = int(registers["A"] / pow(2, combo(operand, registers)))
    registers["B"] = A
    return None

def cdv(operand, registers):
    A = int(registers["A"] / pow(2, combo(operand, registers)))
    registers["C"] = A
    return None

def solve(input_file: str):
    lines = utils.read_lines(input_file)
    registers = {"output": []}
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

    pointer = 0
    steps = 0

    while pointer in range(len(program)):
        opcode = program[pointer]
        operand = program[pointer+1]
        print("pointer:", pointer, "opcode",opcode, "operand",operand, instructions[opcode], registers)
        rcode = instructions[opcode](operand, registers)
        if rcode != None:
            pointer = rcode
        else:
            pointer += 2
        steps +=1
    print(pointer, registers)
    result = ",".join([str(x) for x in registers["output"]])
    print(result)
    return result
