from solver import solve_1, solve_2


def test_part_1():
    output = solve_1("./task_input/test_1.txt")

    if output is None:
        return False

    assert output == "4,6,3,5,6,3,5,2,1,0"

    output_1 = solve_1("./task_input/input.txt")
    print("\nPart 1 solution:", output_1)


def test_part_2():
    # output = solve_2("./task_input/test_2.txt")

    # if output is None:
    #     return True

    # assert output == 117440

    output_2 = solve_2("./task_input/input.txt")
    print("\nPart 2 solution:", output_2)
