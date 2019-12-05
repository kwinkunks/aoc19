# -*- coding: utf-8 -*-
"""
Advent of Code 2019
Day 5
"""


def get_data() -> list:
    with open('day5.txt', 'r') as f:
        data = f.read()
    return [int(x) for x in data.split(',')]


def day5(data: list) -> list:
    """This thing does it all.
    """
    input_ = int(input("What is the input? "))
    output_ = []
    modes = {0: 'pos', 1: 'imm'}
    data = data.copy()
    i, inc = 0, 1

    while True:

        instruction = data[i]

        op = instruction % 100
        mode_1 = modes.get(((instruction % 1000) // 100), 'pos')
        mode_2 = modes.get((instruction // 1000), 'pos')

        if op == 99:
            break

        if op == 1:  # Add
            inc = 4
            x, y, z = data[i+1:i+4]
            x = x if (mode_1 == 'imm') else data[x]
            y = y if (mode_2 == 'imm') else data[y]
            data[z] = x + y
        if op == 2:  # Multiply
            inc = 4
            x, y, z = data[i+1:i+4]
            x = x if (mode_1 == 'imm') else data[x]
            y = y if (mode_2 == 'imm') else data[y]
            data[z] = x * y
        if op == 3:  # Input
            inc = 2
            z = data[i+1]
            data[z] = input_
        if op == 4:  # Output
            inc = 2
            z = data[i+1]
            output_.append(z if (mode_1 == 'imm') else data[z])
        if op == 5:  # Jump to pos par2 if par1 non-zero else do nothing
            inc = 3
            x, y = data[i+1:i+3]
            x = x if (mode_1 == 'imm') else data[x]
            y = y if (mode_2 == 'imm') else data[y]
            if x != 0:
                i = y  # jump
                continue
        if op == 6:  # Jump if false
            inc = 3
            x, y = data[i+1:i+3]
            x = x if (mode_1 == 'imm') else data[x]
            y = y if (mode_2 == 'imm') else data[y]
            if x == 0:
                i = y  # jump
                continue
        if op == 7:  # Less-than
            inc = 4
            x, y, z = data[i+1:i+4]
            x = x if (mode_1 == 'imm') else data[x]
            y = y if (mode_2 == 'imm') else data[y]
            data[z] = 1 if x < y else 0
        if op == 8:  # Equals
            inc = 4
            x, y, z = data[i+1:i+4]
            x = x if (mode_1 == 'imm') else data[x]
            y = y if (mode_2 == 'imm') else data[y]
            data[z] = 1 if x == y else 0
        i += inc

    return output_


if __name__ == "__main__":
    data = get_data()
    print(day5(data))
