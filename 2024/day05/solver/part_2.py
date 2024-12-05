
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
    seen = []
    for i in range(1, len(line)):
        val = line[i]
        if val in rules.get(line[i-1], []):
            line = line.copy()
            line.pop(i)
            line.insert(i-1, val)
            return fix(line, rules)

    print("Sorted", line)
    return line[int(len(line)/2)]

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