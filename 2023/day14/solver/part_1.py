from solver import utils
import copy


class Pos:
    def __init__(self, y, x):
        self.x = x
        self.y = y

    def __add__(self, o):
        return Pos(self.y + o.y, self.x + o.x)

    def __str__(self):
        return f"Pos({self.y}, {self.x})"

    def __repr__(self):
        return f"Pos({self.y}, {self.x})"


def solve(input_file: str):
    lines = [list(x) for x in utils.read_lines(input_file)]

    def traverse(pos, dir, grid):
        new_pos = pos + dir
        if new_pos.x in range(len(grid[0])) and new_pos.y in range(len(grid)):
            if grid[new_pos.y][new_pos.x] == ".":
                return traverse(new_pos, dir, grid)
        return pos

    rocks = []
    dir = Pos(-1, 0)
    new_grid = [[x.replace("O", ".") for x in y] for y in lines]

    sums = []
    for y, line in enumerate(lines):
        for x, chr in enumerate(line):
            if chr == "O":
                # print("Rock", y, x)
                rock = traverse(Pos(y, x), dir, new_grid)
                rocks.append(rock)
                # print("L--> Rock", rock.y, rock.x)
                new_grid[rock.y][rock.x] = "O"
                sums.append(len(lines)-rock.y)

    return sum(sums)
