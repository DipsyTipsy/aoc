from solver import utils


def solve(input_file: str):
    lines = [int(x) for x in utils.read_lines(input_file)[0].split(" ")]

    # 0 -> 1
    # stone % 2 -> (left half stone, right half stone), no leading zero
    # else new stone ->  old stone * 2024

    stones = lines.copy()


    for i in range(25):
        print(stones)

        _new_stones = []
        for stone in stones:
            match stone:
                case stone if len(str(stone))%2 == 0:
                    chr_stone = str(stone)
                    _new_stones.append(int(chr_stone[:int(len(chr_stone)/2)]))
                    _new_stones.append(int(chr_stone[int(len(chr_stone)/2):]))
                    
                case stone if stone == 0:
                    _new_stones.append(1)
                case _:
                    _new_stones.append(stone*2024)

        stones = _new_stones

    print(stones) 
    print(len(stones))

    return len(stones)