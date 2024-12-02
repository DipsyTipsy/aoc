from solver import utils


def solve(input_file: str):
    lines = [[int(y) for y in x.split(" ")] for x in utils.read_lines(input_file)]
    print()

    safe_reports = 0
    for line in lines:
        y = line[0]

        safe = True
        direction = None
        print()
        for i in range(len(line)-1):
            x = line[i+1]
            diff = y - x

            if diff == 0:
                print('UNSAFE NO DIFF')
                safe = False
                break

            if abs(diff) > 3:
                print('UNSAFE MUCH DIFF')
                safe = False
                break

            if direction is not None:
                _direction = diff > 0
                print("DIR: ", diff, direction, _direction)
                if direction is not _direction:
                    print("UNSAFE DIR CHANGE")
                    safe = False
            else:
                direction = diff > 0
                print("Setting dir", direction)

            print(y, x, direction, diff)
                       
            y = x
        
        print(safe, line)
       
        
        if safe:
            safe_reports += 1
    
    print(len(lines))
    
    return safe_reports