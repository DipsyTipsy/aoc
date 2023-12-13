from solver import utils


def solve(input_file: str):
    lines = "\n".join(utils.read_lines(input_file))
    patterns = [x.split("\n") for x in lines.split("\n\n")]
    print()

    for pattern in patterns:
        print()
        for line in pattern:
            print(line)
    
    print("\nSolve")
    for pattern in patterns:
        print()
        # find vertical mirrors
        pattern_len = len(pattern)
        for i in range(len(pattern)):
            from_start, from_end = (i, pattern_len-i-1)
            print(from_start, from_end)
            if pattern[from_start] == pattern[from_end]:
                print(from_start, from_end, pattern[from_start])
        

        # find horizontal mirrors
        # for i, y in enumerate(pattern):
        #     print(i, y)
