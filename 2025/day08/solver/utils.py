from typing import Generator
import functools, time
from collections.abc import Callable

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

def performance_timer[**P, T](func: Callable[P, T]) -> Callable[P, T]:
    """
    Decorator that measures and prints the execution time of a function.

    :param func: The function to be timed.
    :type func: Callable[P, T]
    :return: A wrapper function that times the execution of the decorated function and returns its result.
    :rtype: Callable[P, T]

    .. note::
        Execution times less than 1 second are displayed in milliseconds,
        otherwise they are displayed in seconds. Both with 4 decimals.
    """  # noqa: E501

    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        """
        Wrapper function that times the execution of the decorated function.

        :param args: Positional arguments to pass to the decorated function.
        :param kwargs: Keyword arguments to pass to the decorated function.
        :return: The result of the decorated function.
        :rtype: T
        """
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()

        if (elapsed := end - start) < 1:
            print(f"Elapsed: {(elapsed) * 1_000:.4f}ms")
        else:
            print(f"Elapsed: {(elapsed):.4f}s")

        return res

    return wrapper
