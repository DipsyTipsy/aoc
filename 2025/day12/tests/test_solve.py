from solver import solve_1, solve_2


def test_part_1():
    print("\n# Part 1:")
    output = solve_1("./task_input/test_1.txt")

    if output is None:
        return False

    assert output == 2

    output_1 = solve_1("./task_input/input.txt")
    print("# Part 1 solution:", output_1)


def test_part_2():
    print("\n# Part 2:")
    output = solve_2("./task_input/test_2.txt")

    if output is None:
        return True

    assert output == ...

    output_2 = solve_2("./task_input/input.txt")
    print("# Part 2 solution:", output_2)
