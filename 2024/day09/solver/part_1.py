from solver import utils

def solve(input_file: str):
    lines = utils.read_lines(input_file)[0]
    print()

    disk_map = {}

    #print(lines, len(lines))
    _lines = lines

    index = 0
    while _lines:
        cur = _lines[:2].ljust(2, '0')
        disk_map[index] = (int(cur[0]), int(cur[1]))

        _lines = _lines[2:]
        index += 1

    filesystem = []
    for key, val in disk_map.items():
        files = [str(key) for i in range(val[0])]

        space = "." * val[1]
        filesystem = filesystem + [x for x in files]
        filesystem =  filesystem + [x for x in space]

#    print("Filesystem Before", "".join(filesystem))

    end_index = len(filesystem)-1
    for i, file in enumerate(filesystem):
    #    print(i, file)
        if i >= end_index:
            break
        if "." in file:
            for j in range(end_index, i, -1):
                if filesystem[j] != ".":
                    filesystem[i] = filesystem[j]
                    filesystem[j] = "."
                    end_index = j
                    break

#    print("Filesystem after", "".join(filesystem))
    total = 0
    for i, j in enumerate(filesystem):
        if j != ".":
            total += i*int(j)
    print("Total", total)
    return total