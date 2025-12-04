from solver import utils
dirs = (
    (-1,0),
    (1,0),
    (0,-1),
    (0,1),
    (-1,-1),
    (1,1),
    (1,-1),
    (-1,1),
)

def accessible(rolls):
    total = set()

    for roll in rolls:
        count = 0
        for dir in dirs:
            n_pos = (roll[0]+dir[0], roll[1]+dir[1])
            if n_pos in rolls:
                count += 1
        if count < 4:
            total.add(roll)
    return total



def solve(input_file: str):
    lines = [[y for y in x] for x in utils.read_lines(input_file)]
    rolls = set()
    pos = set()
    for y, line in enumerate(lines):
        for x, str_ in enumerate(line):
            if str_ == "@": 
                rolls.add((y,x))
            else:
                pos.add((y,x))

    total = 0
    rolls_ = accessible(rolls)
    while len(rolls_) > 0:
        total += len(rolls_)
        for pos in rolls_:
            rolls.remove(pos)
        rolls_ = accessible(rolls)

    return total




