from solver import utils
import re

def HASH(step):
    current_value = 0
    for chr in step:
        current_value += ord(chr)
        current_value = current_value * 17
        current_value = current_value % 256
    return current_value

def solve(input_file: str):
    lines = utils.read_lines(input_file)[0].split(",")

    print(lines)
    
    boxes = {x: {} for x in range(256)} 
    for step in lines:
        label, operation, lens = re.findall(r"([a-z]+)([\=|\-])(\d+)?", step)[0]
        box = HASH(label)
        print(step, label, operation, lens, box)

        boxes[box][label] = lens
        if(boxes[box][label] == ''):
            boxes[box].pop(label)
    
    sums = []
    for box_num, box in boxes.items():
        for i, lens in enumerate(box.values()):
            power = 1 * (box_num+1) * (i+1) * int(lens)
            sums.append(power)
    print(sums)

    return sum(sums)



        








