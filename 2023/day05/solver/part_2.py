from solver import utils


def solve(input_file: str):
    lines = list(filter(lambda x: x != "", utils.read_lines(input_file)))

    seeds = [range(int(x), int(x) + int(y)) for x,y in utils.pairwise(lines[0].split(" ")[1:])]

    table = list()
    mapping = []
    for line in lines[2:]:
        if(":" in line):
            table.append(mapping)
            mapping = []
            continue
        mapping.append(line)
    table.append(mapping)
    
    min_loc = 999999999999
    print(seeds)
    for seed_range in seeds:
        sample_scale = int(len(seed_range)*0.0001)
        if(sample_scale <= 0):
            sample_scale = 1
        print(f"Checking {len(seed_range[::sample_scale])} seeds")
        for seed in seed_range[::sample_scale]:
            nx = seed
            cu = seed
            for category in table:
                for map in category:
                    nx = utils.lookup(cu, map)
                    if(nx != cu):
                        break
                
                cu = nx
            if(nx < min_loc):
                min_loc = nx
                min_range = seed_range
        print(f"Current min is: {min_loc}, min_range {min_range}")

    print(f"Checking full range for: {min_range}, {len(min_range)} seeds")
    min_loc = 999999999999
    for seed in min_range:
        nx = seed
        cu = seed
        for category in table:
            for map in category:
                nx = utils.lookup(cu, map)
                if(nx != cu):
                    break
            
            cu = nx
        if(nx < min_loc):
            min_loc = nx
            min_range = seed_range


    print(min_loc)
    return min_loc
