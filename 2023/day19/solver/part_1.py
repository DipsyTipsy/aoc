from solver import utils
import re, math



def solve(input_file: str):
    lines = utils.read_lines(input_file)

    print()
    rules = {}
    part_ratings = []

    for line in lines:
        line = line.replace("}", "").split("{")
        if len(line) == 1:
            continue

        if line[0] != "":
            key = line[0]
            raw_rule = line[1].split(",")
            default = raw_rule[-1]
            workflow = "destination=False\n"
            for rule in raw_rule[:-1]:
                rule_key = rule[0]
                rule_check = rule.split(":")[0][1:]
                rule_result = rule.split(":")[1]
                workflow += f"if part[\"{rule_key}\"]{rule_check} and not destination:\n\tdestination=\"{rule_result}\"\n"
            workflow += f"if not destination:\n\tdestination=\"{default}\""
            rules[key] = workflow 
                

        else:
            ratings = {item.split("=")[0]: int(item.split("=")[1]) for item in line[1].split(",")}
            print("Rating", line, ratings)
            part_ratings.append(ratings)

    def check_part(part, current_rule="in"):
        print(f"Checking: {part} curent_rule: {current_rule}")
        output = {}
        exec(rules[current_rule], {"part": part}, output)
        destination = output.get("destination")
        if destination in ["A", "R"]:
            return destination
        if destination:
            return check_part(part, destination)
        return "R"
        
    
    accepted_parts = []
    for part in part_ratings:
        print()
        status = check_part(part)
        print(f"Check Report: {status}")

        if status == "A":
            part_sum = 0
            for val in part.values():
                part_sum += val
            accepted_parts.append(part_sum)

    return sum(accepted_parts)