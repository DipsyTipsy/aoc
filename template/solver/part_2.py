from solver import utils


@utils.performance_timer
def solve(input_file: str):
    lines = utils.read_lines(input_file)
