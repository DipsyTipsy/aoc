from solver import solve_1, solve_2


# def test_part_1():
#     output = solve_1("./task_input/test_1.txt", 7, 12)

#     if output is None:
#         return False

#     assert output == 22

#     output_1 = solve_1("./task_input/input.txt", 71, 1024)
#     print("\nPart 1 solution:", output_1)


def test_part_2():
    output = solve_2("./task_input/test_2.txt", 7, 1)

    if output is None:
        return True

    assert output == (6,1)

    output_2 = solve_2("./task_input/input.txt", 71, 3000)
    print("\nPart 2 solution:", output_2)
