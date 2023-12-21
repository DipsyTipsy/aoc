from solver import utils
import re, math

def solve(input_file: str):
    lines = utils.read_lines(input_file)

    print()
    workflows = {}
    graph = {"A": "", "R": ""}

    for line in lines:
        line = line.replace("}", "").split("{")
        if len(line) == 1:
            continue

        if line[0] != "":
            key = line[0]

            raw_rule = [x.split(":") for x in line[1].split(",")]
            current_rules = {}
            prev_rules = []
            _raw_rule = [[x for x in y] for y in raw_rule]
            # print()
            for i, rule in enumerate(raw_rule):
                # print(key, rule, current_rules)
                sub_key = rule[-1]
                if len(rule) > 1:
                    _key, operator, value = re.findall(r"([a-z\:]+)([\>\<]+)(\d+)", rule[0])[0]
                    value = int(value)
                    if operator == ">":
                        value += 1
                    else:
                        value -= 1
                    rule = [f"{_key}{operator}{value}", *rule[1:]]

                if len(rule) > 2:
                    current_rules[sub_key] = rule[0]
                elif len(rule) > 1:
                    current_rules[sub_key] = [rule[0]]
                else:
                    sub_key = f"default:{key}"
                    current_rules[sub_key] = []
                    _raw_rule.pop(i)
                    _raw_rule.append([sub_key])
                    graph[sub_key] = [rule[-1]]
                    workflows[f"default:{key}"] = {rule[-1]: []}
                if i > 0:
                    for _rule in prev_rules:
                        _key, operator, value = re.findall(r"([a-z\:]+)([\>\<]+)(\d+)", _rule)[0]
                        value =  int(value)
                        if operator == ">":
                            operator = "<"
                            value -= 1
                        else:
                            operator = ">"
                            value += 1
                        new_rule = f"{_key}{operator}{value}"
                        current_rules[sub_key].append(new_rule)

                prev_rules.append(current_rules[sub_key][0])

            workflows[key] = current_rules
            workflows[f"default:{key}"] = {list(workflows[f"default:{key}"].keys())[0]: current_rules[f"default:{key}"]}

            links = [x[-1] for x in _raw_rule]
            graph[key] = links
        
    for flow in workflows.items():
        print(f"{flow=}")

    def dfs(visited, graph, node, path_str="", path=[]):
        if node not in visited:
            if path_str == "":
                path_str = node
                path = [node]
            else:
                path.append(node)
                path_str += f" -> {node}"

            if node in ["A", "R"]:
                print(path_str)
                paths.append(tuple(path))

            visited.add(node)
            for neighbour in graph[node]:
                dfs(visited.copy(), graph, neighbour, path_str, path.copy())
    
    visited = set()
    paths = []
    dfs(visited, graph, 'in')

    needed_rules = []
    for path in paths:
        path_req = set()
        if "A" in path:
            for cur_rule, next_rule in utils.sliding_window(path, 2, 1):
                # print(cur_rule, next_rule, workflows[cur_rule][next_rule])
                _paths = workflows[cur_rule][next_rule]
                if type(_paths) == list:
                    for _path in _paths:
                        path_req.add(_path)
                        # print(f"{path_req=}")
                else:
                    path_req.add(_paths)
            needed_rules.append(path_req)
            print(path, path_req, sep="\t")
    # print(needed_rules)

    min_value = 1
    max_value = 4000

    total_possibilities = []

    keys = {
        "x": [min_value, max_value], 
        "s": [min_value, max_value], 
        "a": [min_value, max_value], 
        "m": [min_value, max_value], 
        }

    for rules in needed_rules:
        print()
        current_ranges = {x: y.copy() for x,y in keys.items()}
        for rule in rules:
            # print(rule)
            key, operator, value = re.findall(r"([a-z]+)([\>\<]+)(\d+)", rule)[0]
            value = int(value)
            if ">"==operator:
                current_ranges[key][0] = max(current_ranges[key][0], value)
            if "<"==operator:
                current_ranges[key][1] = min(current_ranges[key][1], value)
        print(current_ranges, rules)
        score = 1
        for key, values in current_ranges.items():
            _score = values[1] - values[0] + 1
            score *=_score
            print(values[1], values[0], _score)
        total_possibilities.append(score)
        print("Possibillities", score)

    print("Total Possibillities:", sum(total_possibilities))    
    return sum(total_possibilities)
