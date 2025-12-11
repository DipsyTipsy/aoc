from solver import utils
from collections import defaultdict


@utils.performance_timer
def solve(input_file: str):
    lines = utils.read_lines(input_file)
    machines = defaultdict(list)
    for line in lines:
        tmp = line.split(": ")
        machines[tmp[0]] = tmp[1].split(" ")


    start = "svr"
    end = "out"

    to_end = defaultdict(set)
    to_end[end] = set()

    queue = [(start, set())]
    print(machines)

    visited = defaultdict(lambda: defaultdict(int))

    paths = 0
    while len(queue) > 0:
        cur, seen = queue.pop()
        # print(cur)
        print(cur, seen, len(queue))
        if cur == end:
            if all([x in seen for x in ["fft", "dac"]]):
                paths += 1
                # print("All Found")
            # print("OUT")
            # print()
            continue
        
        next = machines[cur]

        # print(next)

        if cur in ["fft", "dac"]:
            # print("adding", cur)
            seen.add(cur)

        for n in next:
            if n in to_end:
                to_end[cur] = seen | to_end[n]
                if len(to_end[cur]) > 1:
                    paths +=  1
                    print("PATH TO END", cur, n)
                    continue

            visited[n][str(seen)] += 1
            if visited[n][str(seen)] < 1000:
                queue += [(n, seen.copy())]
        # [visited[n]+=1 for n in next]
        # print(cur, next, seen)
    
        # print()
    
    for v in visited.items():
        print(v)
    return paths
    