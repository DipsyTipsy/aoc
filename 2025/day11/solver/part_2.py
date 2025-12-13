from solver import utils
from collections import defaultdict


def optimize_machines(machines, stops, start):
    print("Unoptimized")
    for machine in machines.items():
        print(machine)


    changed = True
    i = 0
    cur = start
    while changed and i< 10:
        changed = False
        i +=1

        n_links = []
        for next in machines[cur]:
            print(next)
            if next in stops:
                print("Found something")
                n_links.append(next)
                continue
            else:
                for n in machines[next]:
                    if n not in machines[cur] and n not in n_links:
                        n_links += [n]
            

        print("Setting machine", cur, "to", n_links)
        if machines[cur] != n_links:
            changed = True
        machines[cur] = n_links
        

    print("Optimized")
    for machine in machines.items():
        print(machine)

    return machines



@utils.performance_timer
def solve(input_file: str):
    lines = utils.read_lines(input_file)
    machines = defaultdict(list)
    for line in lines:
        tmp = line.split(": ")
        machines[tmp[0]] = set(tmp[1].split(" "))


    stops = ["fft", "dac"]
    monitor = ["fft", "axv", "erd"]
    start = "svr"
    end = ["out"]

    end = set(end)

    print(machines)
    # machines = optimize_machines(machines, stops, start)
    # return


    paths = 0
    depth = 0

    for i in range(2):
        print(i)
        paths = 0
        visited = defaultdict(int)
        queue = [(start, set())]
        while len(queue) > 0:
            depth +=1
            cur, seen = queue.pop()
            visited[cur] +=1
            # if cur in end:
            #     num_correct = sum([x in seen for x in stops])
            #     if num_correct > 1:
            #         paths += 1
            #         continue

            
            next = machines[cur].copy()
            seen.add(cur)

            next_ = set()
            if depth % 100000 == 0:
                print(cur, "score", paths, "depth", len(seen), len(machines), len(end), "visited_nodes", len(visited), "visited", visited[cur], "count", depth, "queue",len(queue))
                queue = sorted(queue, key=lambda tup: visited[tup[0]], reverse=True)
                # for q in queue:
                #     print(q)
                # return

            if len(next) == 0:
                end.add(cur)
                continue

            
            touched_end = False
            while len(next) > 0:
                n = next.pop()
                print()
                print(n, str(seen), )
                if not n in seen:
                # if True:
                    if n in end:
                        touched_end = True
                        num_correct = sum([x in seen for x in stops])
                        # print()
                        # print("Found end", cur, n, num_correct, seen)
                        # print()
                        if num_correct > 1:
                            paths += 1
                        
                        if num_correct > 0:
                            next_.add(n)

                    # else:
                    #     next_.add(n)
                    #     queue.append((n, seen.copy()))
                    elif n in stops:
                        print("Found stop", cur, n)
                        queue.append(((n, seen.copy())))
                        next_.add(n)

                    else:
                        for x in machines[n]:
                            # if x not in stops:
                            print("not stop")
                            x_seen = seen.copy()
                            x_seen.add(x)
                            queue.append(((x, x_seen.copy())))
                            next_.add(x)
                else: 
                    print("Cycle")
                    # return

                    #     # else:
                        #     next_.add(n)
                        #     queue.append((n, seen.copy()))

                        # to_add = (n, seen.copy())
                        # # if visited[n] > cur_visited:
                        # #     queue.insert(0, to_add)
                        # # else:
                        # queue.append(to_add)
                        # next_ += [n]
                # else:
                #     if depth % 10000 == 0:
                #         print("cycle")
                #         return
            
            print("Machine pointer moved from", cur, machines[cur], "To", next_)
            if len(next_) == 0 and touched_end:
                end.add(cur)
            else:
                machines[cur] = next_

    for v in visited.items():
        print(v)
    
    print()
    for m in machines.items():
        print(m)

    print("Ends", end)

    print("Connected to end", len(end), "Machines", len(machines))
    print("Paths found", paths)
    return paths
    
    # 23957358
    # 7985790
    # 610335
    # 4272345