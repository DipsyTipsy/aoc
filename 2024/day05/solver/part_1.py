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

def solve(input_file: str):
    lines = utils.read_lines(input_file)
    rules = defaultdict(list)
    [rules[int(x.split("|")[0])].append(int(x.split("|")[1])) for x in lines if "|" in x]
    ordering = [[int(y) for y in x.split(",")] for x in lines if "," in x]
    print()
    
  #  print(f"Rules: {rules}")
  #  print(f"Order: {ordering}")

    total = 0
    for line in ordering:
  #      print()
        cur_rules = {k: rules[k] for k in rules.keys() if k in line}
  #      print(line)
  #      print("cur", cur_rules)
        total += check(line, cur_rules)

    print(total)
    return total






