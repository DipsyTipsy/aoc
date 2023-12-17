from typing import Generator


def read_lines(input_file: str):
    with open(input_file) as f:
        return [line.strip() for line in f.readlines()]


def read_numbers(input_file: str):
    with open(input_file) as f:
        return [int(num) for num in f.read().split(",")]


def sliding_window(
    array: list, window: int, step: int | None = None
) -> Generator[list, None, None]:
    if step is None:
        step = window

    for i in range(0, len(array) - window + 1, step):
        yield array[i : i + window]


def out_of_bounds(row: int, col: int, matrix: list[list]):
    if row < 0 or row >= len(matrix):
        return True

    if col < 0 or col >= len(matrix[0]):
        return True

    return False


def get_adjacent(
    row: int, col: int, matrix: list[list], width: int = 1, height: int = 1
) -> tuple[int, int]:
    skip_positions = [(row + i, col + j) for i in range(height) for j in range(width)]
    adjacent = []
    for i in range(row - 1, row + 1 + height):
        for j in range(col - 1, col + 1 + width):
            # Skip current position
            if (i, j) in skip_positions:
                continue

            # Check if out of bounds
            if out_of_bounds(row, col, matrix):
                continue

            adjacent.append((i, j))

    return adjacent

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

def traverse(pos: Pos, dir: Pos, grid, empty_space = "."):
        new_pos = pos + dir
        if new_pos.x in range(len(grid[0])) and new_pos.y in range(len(grid)):
            if grid[new_pos.y][new_pos.x] == empty_space:
                return traverse(new_pos, dir, grid)
        return (pos, new_pos, grid[new_pos.y][new_pos.x])

def get_pos_chr(pos: Pos, dir: Pos, grid, empty_space = "."):
        new_pos = pos + dir
        if new_pos.x in range(len(grid[0])) and new_pos.y in range(len(grid)):
            return (grid[new_pos.y][new_pos.x], new_pos)
        return ("", None)