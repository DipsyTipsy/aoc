from solver import solve_1, solve_2


def test_part_1():
    output = solve_1("./task_input/test_1.txt", 6)

    if output is None:
        return False

    assert output == 16

    output_1 = solve_1("./task_input/input.txt", 64)
    print("\nPart 1 solution:", output_1)


def test_part_2():
    output = solve_2("./task_input/test_2.txt", 6)
    assert output == 16
    output = solve_2("./task_input/test_2.txt", 10)
    assert output == 50
    output = solve_2("./task_input/test_2.txt", 50)
    assert output == 1594
    output = solve_2("./task_input/test_2.txt", 100)
    assert output == 6536

    output_2 = solve_2("./task_input/input.txt")
    print("\nPart 2 solution:", output_2)
