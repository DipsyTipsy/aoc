from solver import solve_1, solve_2


def test_part_1():
    output = solve_1("./task_input/test_1.txt", 7, 11)

    if output is None:
        return False

    assert output == 12

    output_1 = solve_1("./task_input/input.txt", 103, 101)
    print("\nPart 1 solution:", output_1)


def test_part_2():
    output_2 = solve_2("./task_input/input.txt", 103, 101)
    print("\nPart 2 solution:", output_2)
