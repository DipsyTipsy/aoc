from solver import utils
from collections import defaultdict

def calculate(input, loops):
    print(input)
    stones = input.copy()
    known_patterns = defaultdict(lambda: defaultdict(list))
    for i in range(loops):
        print("Iteration",i, "known patterns", len(known_patterns), "Stones",len(stones))
        new_stones = []

        for stone in stones:
            _new_stones = []
            match stone:
                case stone if stone in known_patterns:
                    known_patterns[stone]["index"].append(i)
                case stone if stone == 0:
                    _new_stones.append(1)
                    known_patterns[stone]["targets"].append(1)
                case stone if len(str(stone))%2 == 0:
                    chr_stone = str(stone)
                    a = int(chr_stone[:int(len(chr_stone)/2)])
                    b = int(chr_stone[int(len(chr_stone)/2):])
                    _new_stones.append(a)
                    _new_stones.append(b)
                    known_patterns[stone]["index"].append(i)
                    known_patterns[stone]["targets"].append(a)
                    known_patterns[stone]["targets"].append(b)
                case _:
                    _new_stones.append(stone*2024)
                    known_patterns[stone]["index"].append(i)
                    known_patterns[stone]["targets"].append(stone*2024)

            new_stones += _new_stones
 
        stones = new_stones

    print("Iteration",i+1, "known patterns", len(known_patterns), "Stones",len(stones))

    return known_patterns

def solve(input_file: str):
    lines = [int(x) for x in utils.read_lines(input_file)[0].split(" ")]

    #result = calculate(lines, 75)
    target_depth = 1
    result = calculate([125, 17], target_depth+1)


    total_stones = 0
    for pattern, vals in result.items():
        print("Checking Pattern", pattern, "Indexes", vals['index'], "Targets", vals["targets"])
        for target in vals['targets']:
            for start  in vals["index"]:
                print(target, start)


    print(total_stones)