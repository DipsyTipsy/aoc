from solver import utils


def solve(input_file: str):
    def sub_arr(arr: list):
        return arr[0] - arr[1] 

    lines = [ [int(y) for y in x.split()] for x in utils.read_lines(input_file)]
    
    estimates = []
    for line in lines:
        level = 0
        data = [line]

        while any(data[level]):
            data.append([sub_arr(x) for x in utils.sliding_window(data[level], 2, 1)])
            level += 1

        estimate = sum([x[0] for x in data])
        estimates.append(estimate)

    return sum(estimates)
