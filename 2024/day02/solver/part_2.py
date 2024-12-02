from solver import utils


def check_line(line):
    y = line[0]
    safe = True
    unsafe_counter = 0
    direction = None
    for i in range(len(line)-1):
        x = line[i+1]
        diff = y - x

        if diff == 0:
            unsafe_counter += 1
#            print(y,x,'UNSAFE NO DIFF')
            safe = False
            continue

        if abs(diff) > 3:
            unsafe_counter += 1
#            print(y, x, 'UNSAFE MUCH DIFF')
            safe = False
            continue

        if direction is not None:
            _direction = diff > 0
            if direction is not _direction:
                unsafe_counter += 1
#                print(y, x, "UNSAFE DIR CHANGE")
                safe = False
                continue
        else:
            direction = diff > 0

#        print(y, x, direction, diff)
                    
        y = x
    safe_str = "UNSAFE"
    if safe:
        safe_str = "SAFE"
    
    print(f"{safe_str} error_count: {unsafe_counter} input: {line}")

    return unsafe_counter

def solve(input_file: str):
    lines = [[int(y) for y in x.split(" ")] for x in utils.read_lines(input_file)]
    print()

    safe_reports = 0
    for line in lines:
        print()
        print(f"Checking {line}")

        for i in range(len(line)):
            cur_line = line.copy()
            cur_line.pop(i)
            safe_counter = check_line(cur_line)
            if safe_counter == 0:
                safe_reports +=1
                break
    
    return safe_reports

