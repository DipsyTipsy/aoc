from solver import utils


def solve(input_file: str):
    lines = [list(x) for x in utils.read_lines(input_file)]
    print()

    current_pos = utils.Pos(0, 0)
    current_dir = utils.Pos(0, 1)

    beams = [[current_pos, current_dir]]

    for line in lines:
        print(line)
    for beam in beams:
        print(beam)
    
    for i in range(4):
        for j, beam in enumerate(beams):
            new_pos, col_pos, chr = utils.traverse(beam[0], beam[1], lines)

            match chr:
                case "|":
                    print(f"Splitting {j} |")
                    if abs(beam[1].x) == 1:
                        beam = [col_pos, utils.Pos(-1, 0)]
                        beams.append([col_pos, utils.Pos(1, 0)])
                    else:
                        beam = [col_pos, beam[1]]
                case "-":
                    print(f"Splitting {j} -")
                    if abs(beam[1].y) == 1:
                        beam = [col_pos, utils.Pos(0, -1)]
                        beams[j].append([col_pos, utils.Pos(0, 1)])
                    else:
                        beam = [col_pos, beam[1]]
                case "/":
                    print("mirror")
                case "\\":
                    print("mirror")
                case ".":
                    print("Out of bounds")
                    beams.pop(j)
            
            print(f"Loop:{i} Beam:{j}:{beam[0]} -> {new_pos}")
        print()
    print(beams)
