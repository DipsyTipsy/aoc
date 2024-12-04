from solver import utils

def search(map, y, x, dir):
    hit = 0
    new_y = y + dir[0]
    new_x = x + dir[1]
    try:
        if new_y < 0 or new_x < 0:
            return ""
        return map[new_y][new_x]
    except IndexError:
        return ""

def solve(input_file: str):
    lines = [[y for y in x] for x in utils.read_lines(input_file)]

    total = 0 
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "A":
                diags = []

                diags.append(search(lines, y, x, (1,1)) + "A" + search(lines, y, x, (-1,-1)))
                diags.append(search(lines, y, x, (-1,1)) + "A" + search(lines, y, x, (1,-1)))

                total += sum([all([x in diag for x in ["M", "A", "S"]]) for diag in diags]) == 2
   
    return total