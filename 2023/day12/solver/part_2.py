from solver import utils
from collections import Counter
from itertools import product


def solve(input_file: str):
    lines = [x for x in utils.read_lines(input_file)]

    print()
    print("INPUT")
    for line in lines:
        print(line)

    def check_record(spring, record):
        if len(spring) != len(record):
            return False
        return all([len(x)==y for x,y in zip(spring, record)])
    
    print("\nSOLVE")
    def filler(word: str, from_char: str, possibillities: tuple):
        options = [(c,) if c != from_char else possibillities for c in word]
        return (''.join(o) for o in product(*options))

    possibillities = []
    for line in lines:
        spring, record = line.split()
        spring =  "?".join([spring] * 5)
        record = ",".join([record] * 5)
        print(spring, record)
        record = [int(x) for x in record.split(",")]

        poss = 0
        total_springs = sum(record)
        for perm in filler(spring, "?", ("#", ".")):
            if perm.count("#") != total_springs:
                continue
            arr_spring = list(filter(lambda x: len(x) > 0, perm.split(".")))
            #print(arr_spring, perm)
            if check_record(arr_spring, record):
                poss += 1

        #print(spring, record, poss)
        possibillities.append(poss)

    #print(possibillities)


    print(sum(possibillities))

    return sum(possibillities)

