
from solver import utils
from collections import defaultdict

def check(line, rules):
    history = []
    for val in line:
        #print(val, rules.get(val))
        if any([x for x in rules.get(val, "foobar") if x  in history]):
  #          print("invalid")
            return 0
        else:
            history.append(val)
  #  print("Valid:", history)
    value = history[int(len(history)/2)]
  #  print("Returing: ", value)
    return value

def fix(line, rules):
    print(line)
    for val in line:
        cur_line = line.copy()
        cur_line.remove(val)
        print("- Starting check from", val)
        test = _fix(cur_line, [val], rules)
        print("fix result", test)
        if test > 0:
            print("Sorted: ", test)
            return test

    return test

def _fix(neighbors, path, rules):
    if len(neighbors) == 1:
        print("END", path+neighbors)
        val = check(path+neighbors, rules)
        if val > 0:
            return val
        else:
            return 0
    
    possible_neighbors = [val for val in neighbors if val in rules.get(path[-1], [])]

    for val in possible_neighbors:
        cur_line = neighbors.copy()
        cur_line.remove(val)
        if check(path+[val], rules) > 0:
            further_check =  _fix(cur_line, path + [val], rules)
            if further_check > 0:
                return further_check
        else:
            continue

    return  0


def solve(input_file: str):
    print("start of part 2")
    lines = utils.read_lines(input_file)
    rules = defaultdict(list)
    [rules[int(x.split("|")[0])].append(int(x.split("|")[1])) for x in lines if "|" in x]
    ordering = [[int(y) for y in x.split(",")] for x in lines if "," in x]
    print()
    

    total = 0
    for line in ordering:
        cur_rules = {k: rules[k] for k in rules.keys() if k in line}
        cur_check = check(line, cur_rules)
        if cur_check == 0:
            print()
            print("Wrong, checking", line)
            total += fix(line, cur_rules)


    print(total)
    return total