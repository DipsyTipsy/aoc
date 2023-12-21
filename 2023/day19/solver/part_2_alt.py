from solver import utils
import re, math

def solve(input_file: str):
    lines = utils.read_lines(input_file)

    print()
    workflows = {}
    part_ratings = []

    for line in lines:
        line = line.replace("}", "").split("{")
        if len(line) == 1:
            continue

        if line[0] != "":
            key = line[0]
            raw_rule = [x.split(":") for x in line[1].split(",")]
            workflows[key] = raw_rule
        
    for key, rules in workflows.items():
        print(rules)

    def find_links(current_key, destination_key, visited, path):
        visited[current_key] = True
        path.append(current_key)

        if current_key == "A":
            print()
            return tally + current_key
        if current_key == "R":
            return tally + ""

        if current_key in workflows:
            rules = workflows[current_key]
        else:
            print("Something is wrong")
            return False

        for rule in rules:
            link = find_links(rule[-1], tally)
            tally += f"{rule[-1]}->{link}"

        return tally