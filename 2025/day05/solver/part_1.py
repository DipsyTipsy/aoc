from solver import utils


def solve(input_file: str):
    lines = utils.read_lines(input_file)
    ranges, ids = [],[]
    for line in lines:
        if "-" in line:
            min_,max_ = (int(x) for x in line.split("-"))
            range_ = range(min_-1,max_+1)
            ranges.append(range_)
        elif len(line) > 0:
            ids.append(int(line))
    
    count = 0
    for id in ids:
        if any(id in range_ for range_ in ranges):
            count +=1
    return count



