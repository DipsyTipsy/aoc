from solver import utils

def update_ranges(ranges):
    check = range

    for i in range(10000):
        range_ = ranges.pop(0)
        min_ = range_.start
        max_ = range_.stop
        added = False
        for i, check in enumerate(ranges):
            if (min_ in check) or (max_+1 in check) or (check.start in range_) or (check.stop in range_):
                a = min(check.start, min_)
                b = max(check.stop, max_+1)
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
            print(line)
            min_,max_ = (int(x) for x in line.split("-"))
            range_ = range(min_,max_+1)
            if len(ranges) == 0:
                range_ = range(min_,max_+1)
                ranges.append(range_)
                print("init",range_)
                continue
            added = False
            for i, check in enumerate(ranges):
                if (min_ in check) or (max_+1 in check) or (check.start in range_) or (check.stop in range_):
                    a = min(check.start, min_)
                    b = max(check.stop, max_+1)
                    print(check, range_, "new", range(a,b))
                    check = range(a,b)
                    ranges[i] = check
                    added = True
            if not added:
                range_ = range(min_,max_+1)
                print("No ranges changed",range_)
                ranges.append(range_)
    
    print()
    print(ranges)
    update_ranges(ranges)
    print(ranges)
    total = 0
    total_set = []
    for range_ in ranges:
        total +=  len(range_)

    print(total)
    return total