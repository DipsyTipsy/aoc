from solver import utils

def distance(a,b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

def area(a,b):
    x = max(a[0],b[0]) - min(a[0],b[0])+1
    y = max(a[1],b[1]) - min(a[1],b[1])+1
    return x*y

def solve(input_file: str):
    lines = [tuple([int(x) for x in line.split(",")]) for line in utils.read_lines(input_file)]

    distances = {}
    for a in lines:
        for b in lines:
            distances[area(a,b)] = [a,b]
    
    max_ = max(distances.keys())
    return area(*distances[max_])


