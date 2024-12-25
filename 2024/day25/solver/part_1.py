from solver import utils


def solve(input_file: str):
    lines = utils.read_lines(input_file).split("\n\n")

    keys = []
    locks = []
    for line in lines:
        current = line.split("\n")
        c_type = "lock"
        if current[0][0] == ".":
            c_type = "key"

        heights = [-1]*len(current[0])
        for x in range(len(current[0])):
            for i in range(len(current)):
                if c_type == "key" and current[i][x] == "#":
                    heights[x] += 1
                elif c_type == "lock" and current[i][x] == "#":
                    heights[x] += 1
        
        match c_type:
            case "lock":
                locks.append(heights)
            case "key":
                keys.append(heights)

    
    fits = set()
    for lock in locks:
        for key in keys:
            if all([(x + y) < 6 for x,y in zip(lock, key)]):
                fits.add(str((lock,key)))
    
    return len(fits)

            

