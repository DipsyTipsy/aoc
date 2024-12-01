from solver import utils


def solve(input_file: str):
    lines = utils.read_lines(input_file)
    a = []
    b = []

    for line in lines:
        data  = line.split("  ")
        a.append(int(data[0]))
        b.append(int(data[1]))


    a.sort()
    b.sort()

    distance = 0
    for i in range(len(a)):
        distance += abs(a[i]-b[i])
    
    return distance
