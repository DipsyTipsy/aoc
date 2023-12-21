from solver import utils
from collections import Counter
from itertools import product
import re


def solve(input_file: str):
    lines = [x for x in utils.read_lines(input_file)]

    print()
    print("INPUT")

    springs = []
    records = []
    for line in lines:
        spring, record = line.split()
        spring =  "?".join([spring] * 5)
        record = ",".join([record] * 5)
        springs.append(spring)
        records.append([int(x) for x in record.split(",")])
        print(len(spring), spring, record)
    
    for spring, record in zip(springs, records):
        print(spring, record)
        permutations = [""]

        for chr in spring:
            for i, perm in enumerate(permutations):
                if chr == "?":
                    permutations[i] += "."
                    permutations.append(perm + "#")

            print(chr)
        
        print(permutations)


    

    def check_record(spring, record):
        if len(spring) != len(record):
            return False
        return all([len(x)==y for x,y in zip(spring, record)])
    
    # print("\nSOLVE")
    # def filler(word: str, from_char: str, possibillities: tuple):
    #     options = [(c,) if c != from_char else possibillities for c in word]
    #     return (''.join(o) for o in product(*options) if o.count("#") == total_springs and re.findall(r"#+", ''.join(o)) == num_springs)

    # possibillities = []
    # total_perms_checked = 0
    # for line in lines:
    #     spring, record = line.split()
    #     spring =  "?".join([spring] * 5)
    #     record = ",".join([record] * 5)
    #     print(spring, record)
    #     record = [int(x) for x in record.split(",")]


    #     poss = 0
    #     total_poss = 0
    #     total_springs = sum(record)
    #     num_springs = ["#"*x for x in record]
    #     perms = filler(spring, "?", ("#", "."))

    #     for perm in perms:
    #         print(total_poss)
    #         arr_spring = list(filter(lambda x: len(x) > 0, perm.split(".")))
    #         if check_record(arr_spring, record):
    #             #print("   ",perm)
    #             poss += 1
    #         else:
    #             print(perm)

    #         total_poss +=1
    #     print(total_poss, poss)
    #     total_perms_checked +=total_poss

    #     #print(spring, record, poss)
    #     possibillities.append(poss)

    # print(total_perms_checked)


    # print(sum(possibillities))

    # # return sum(possibillities)

