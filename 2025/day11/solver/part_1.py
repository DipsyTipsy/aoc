from solver import utils
from collections import defaultdict


@utils.performance_timer
def solve(input_file: str):
    lines = utils.read_lines(input_file)
    machines = defaultdict(list)
    for line in lines:
        tmp = line.split(": ")
        machines[tmp[0]] = tmp[1].split(" ")


    start = "you"
    end = "out"

    queue = [start]

    paths = 0
    while len(queue) > 0:
        cur = queue.pop()
        if cur == end:
            paths += 1
        
        next = machines[cur]
        queue += next
        # print(cur, next)
    
    return paths




