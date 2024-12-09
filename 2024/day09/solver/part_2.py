from solver import utils
from collections import defaultdict
from copy import deepcopy


def solve(input_file: str):
    lines = utils.read_lines(input_file)[0]
    print()

    disk_map = {}

    #print(lines, len(lines))
    _lines = lines

    index = 0
    while _lines:
        cur = _lines[:2].ljust(2, '0')
        files = [str(index) for i in range(int(cur[0]))]
        space = ["." for i in range(int(cur[1]))]
        disk_map[index] = [files+space, int(cur[0]), int(cur[1])]

        _lines = _lines[2:]
        index += 1


    print(disk_map)
    moved_items = set()
    to_copy = deepcopy(disk_map)

    filesystem = []
    _new_map = deepcopy(disk_map)

    for id, disk in reversed(disk_map.items()):
        disk[0] = _new_map[id][0]
        for c_id in range(id):
            c_disk = _new_map.get(c_id)
            if c_disk:
                if c_disk[2] >= disk[1]:
                    print("Can move",  id, "->", c_id)
                    # Fix new pos
                    free_space = c_disk[2] - disk[1]
                    #n_disk = [x for x in "".join(c_disk[0]).replace("."*disk[1], str(id)*disk[1],1)]
                    n_disk = c_disk[0][:c_disk[1]] + [str(id)]*disk[1] + ["."]*free_space
                    print(n_disk, "."*c_disk[2], str(id)*disk[1])
                    _new_map[c_id] = [n_disk, c_disk[1]+disk[1], free_space]
                    print(n_disk)

                    # Fix old pos
                    #print(disk[0])
                    n_disk = []
                    for x in disk[0]:
                        if x == str(id):
                            n_disk.append(".")
                        else:
                            n_disk.append(x)

                    _new_map[id] = [n_disk, 0, disk[2]]
                    break

    
    for id, disk in _new_map.items():
        filesystem += disk[0]


    #for id, disk in disk_map.items():
    #    if id not in moved_items:
    #        files = [str(id) for i in range(disk[0])]
    #        filesystem += files

    #    free_space = disk[1]
    #    if free_space > 0:
    #        print("WE GOT SPACE", id, disk)
    #        _to_copy = deepcopy(to_copy)
    #        for c_id, c_disk in reversed(_to_copy.items()):
    #            print(id, c_id)
    #            if free_space >= c_disk[0] and c_id > id:
    #                print("Moving", c_id, c_disk)
    #                free_space -= c_disk[0]

    #                moved_items.add(c_id)
    #                to_copy.pop(c_id)
    #                filesystem += [str(c_id) for i in range(c_disk[0])]
    #    for i in range(free_space):
    #        filesystem.append(".")
    #        
    #    print(id, disk)

    print(filesystem)


    print("Filesystem after", "".join(filesystem))
    total = 0
    for i, j in enumerate(filesystem):
        if j != ".":
            total += i*int(j)
    print("Total", total)
    return total

