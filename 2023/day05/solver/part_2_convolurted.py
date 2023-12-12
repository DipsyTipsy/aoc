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
    
    def find_possible_low_location_seeds(seeds, table, minimum):
        def find_lowest_range(table: list, minimum: int=0):
            min_dest = 99999999999999999
            min_src = 99999999999999999
            min_dest_range = None
            min_src_range = None
            for line in table:
                dest, src, length = tuple([int(x) for x in line.split(" ")])
                if dest < min_dest and dest >= minimum:
                    min_dest = dest
                    min_dest_range = range(dest, dest + length)
                    min_src_range = range(src, src + length)
                
                if src < min_src:
                    min_src = src
            
            if (min_dest != minimum and min_src != minimum):
                min_src_range = range(minimum, min(min_src, min_dest))
            
            return min_src_range
        
        def find_overlapping_range(table: list, dest_range: range):
            best_range = []
            for line in table:
                dest, src, length = tuple([int(x) for x in line.split(" ")])
                if dest <= dest_range.stop and dest >= dest_range.start:
                    best_range.append(range(src, min(src + (dest_range.stop - dest), src + length)))

            return None if len(best_range) == 0 else best_range

        target_range = find_lowest_range(table[-1], minimum)
        min_range_value = target_range.stop
        print(f"min final range is {target_range}")

        next_ranges = find_overlapping_range(table[-2], target_range)
        if next_ranges == None:
            next_ranges = [target_range]

        for category in table[-3::-1]:
            found_ranges = []
            for target_range in next_ranges:
                result = find_overlapping_range(category, target_range)
                if(result):
                    found_ranges = [*result, *found_ranges]
        
        print(f"Ranges that lead to low locations: {found_ranges}")
        possible_seeds = []
        for found_range in found_ranges:
            for seed_range in seeds:
                if seed_range.start <= found_range.stop and seed_range.start >= found_range.start:
                    possible_seeds.append(range(seed_range.start, min(seed_range.stop, found_range.stop)))
        print(f"Possible low location seeds: {possible_seeds}")
        return (min_range_value, possible_seeds)


    min_range_value, possible_seeds = find_possible_low_location_seeds(seeds, table, 0)
    if(len(possible_seeds)==0):
        min_range_value, possible_seeds = find_possible_low_location_seeds(seeds, table, min_range_value)
    

    if(len(possible_seeds)==0):
        min_range_value, possible_seeds = find_possible_low_location_seeds(seeds, table, min_range_value)

    
    if(len(possible_seeds)==0):
        min_range_value, possible_seeds = find_possible_low_location_seeds(seeds, table, min_range_value)
    return 46

    min_loc = 999999999999
    seed_run = possible_seeds
    if(len(possible_seeds)==0):
        seed_run = seeds
    for seed_range in seed_run:
        for seed in seed_range:
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
        print(f"Current min is: {min_loc}, current range is: {seed_range}")

    print(min_loc)
    return min_loc