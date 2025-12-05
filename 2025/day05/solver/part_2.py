from solver import utils

def update_ranges(ranges):
    for i in range(200):
        range_ = ranges.pop(0)
        added = False
        for i, check in enumerate(ranges):
            if (range_.stop > check.start and check.stop > range_.start):
                a = min(check.start, range_.start)
                b = max(check.stop, range_.stop)
                check = range(a,b)
                ranges[i] = check
                added = True
        if not added:
            ranges.append(range_)

def solve(input_file: str):
    lines = utils.read_lines(input_file)
    ranges, ids = [],[]
    for line in lines:
        if "-" in line:
            min_,max_ = (int(x) for x in line.split("-"))
            ranges.append(range(min_,max_+1))
   
    update_ranges(ranges)
    total = sum(len(x) for x in ranges)

    return total