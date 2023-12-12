from solver import utils


def solve(input_file: str):
    lines = list(filter(lambda x: x != "", utils.read_lines(input_file)))

    seeds = [int(x) for x in lines[0].split(" ")[1:]]

    table = list()
    mapping = []
    for line in lines[2:]:
        if(":" in line):
            table.append(mapping)
            mapping = []
            continue
        mapping.append(line)
    table.append(mapping)
    
    locations = []
    for seed in seeds:
        nx = seed
        cu = seed
        for category in table:
            for map in category:
                nx = utils.lookup(cu, map)
                if(nx != cu):
                    break
            
            cu = nx
        locations.append(nx)

    print(locations)
    return min(locations)