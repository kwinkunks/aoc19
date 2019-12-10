# -*- coding: utf-8 -*-
"""
Advent of Code 2019
Day 9
"""


def get_data() -> list:
    with open('day9.txt', 'r') as f:
        data = f.read()
    return [int(x) for x in data.split(',')]


def execute(prog: list, input_: int=0) -> list:
    """This thing does it all.
    """
    output_ = []
    modes = {0: 'pos', 1: 'imm', 2: 'rel'}
    data: dict = {i: d for i, d in enumerate(prog)}
    i, inc = 0, 1
    BASE = 0

    while True:
        instruction = data.get(i, -1)

        op = instruction % 100
        mode_1 = modes.get(((instruction % 1000) // 100), 'pos')
        mode_2 = modes.get(((instruction % 10_000) // 1000), 'pos')
        mode_3 = modes.get((instruction // 10_000), 'pos')

        if op == -1:
            print("Something went wrong")
            break

        if op == 99:
            break

        if op == 1:  # Add
            inc = 4
            x, y, z = [data.get(i+j, 0) for j in range(1, inc)]
            x = x if (mode_1 == 'imm') else data.get(x+BASE, 0) if (mode_1 == 'rel') else data.get(x, 0)
            y = y if (mode_2 == 'imm') else data.get(y+BASE, 0) if (mode_2 == 'rel') else data.get(y, 0)
            z = z+BASE if (mode_3 == 'rel') else z
            data[z] = x + y
        if op == 2:  # Multiply
            inc = 4
            x, y, z = [data.get(i+j, 0) for j in range(1, inc)]
            x = x if (mode_1 == 'imm') else data.get(x+BASE, 0) if (mode_1 == 'rel') else data.get(x, 0)
            y = y if (mode_2 == 'imm') else data.get(y+BASE, 0) if (mode_2 == 'rel') else data.get(y, 0)
            z = z+BASE if (mode_3 == 'rel') else z
            data[z] = x * y
        if op == 3:  # Input
            inc = 2
            z = data[i+1]
            z = z+BASE if (mode_1 == 'rel') else z
            data[z] = input_
        if op == 4:  # Output
            inc = 2
            z = data[i+1]
            z = z if (mode_1 == 'imm') else data.get(z+BASE, 0) if (mode_1 == 'rel') else data.get(z, 0)
            output_.append(z)
        if op == 5:  # Jump to pos par2 if par1 non-zero else do nothing
            inc = 3
            x, y = [data.get(i+j, 0) for j in range(1, inc)]
            x = x if (mode_1 == 'imm') else data.get(x+BASE, 0) if (mode_1 == 'rel') else data.get(x, 0)
            y = y if (mode_2 == 'imm') else data.get(y+BASE, 0) if (mode_2 == 'rel') else data.get(y, 0)
            if x != 0:
                i = y  # jump
                continue
        if op == 6:  # Jump if false
            inc = 3
            x, y = [data.get(i+j, 0) for j in range(1, inc)]
            x = x if (mode_1 == 'imm') else data.get(x+BASE, 0) if (mode_1 == 'rel') else data.get(x, 0)
            y = y if (mode_2 == 'imm') else data.get(y+BASE, 0) if (mode_2 == 'rel') else data.get(y, 0)
            if x == 0:
                i = y  # jump
                continue
        if op == 7:  # Less-than
            inc = 4
            x, y, z = [data.get(i+j, 0) for j in range(1, inc)]
            x = x if (mode_1 == 'imm') else data.get(x+BASE, 0) if (mode_1 == 'rel') else data.get(x, 0)
            y = y if (mode_2 == 'imm') else data.get(y+BASE, 0) if (mode_2 == 'rel') else data.get(y, 0)
            z = z+BASE if (mode_3 == 'rel') else z
            data[z] = 1 if x < y else 0
        if op == 8:  # Equals
            inc = 4
            x, y, z = [data.get(i+j, 0) for j in range(1, inc)]
            x = x if (mode_1 == 'imm') else data.get(x+BASE, 0) if (mode_1 == 'rel') else data.get(x, 0)
            y = y if (mode_2 == 'imm') else data.get(y+BASE, 0) if (mode_2 == 'rel') else data.get(y, 0)
            z = z+BASE if (mode_3 == 'rel') else z
            data[z] = 1 if x == y else 0
        if op == 9:  # Update BASE
            inc = 2
            z = data[i+1]
            z = z if (mode_1 == 'imm') else data.get(z+BASE, 0) if (mode_1 == 'rel') else data.get(z, 0)
            BASE += z
        i += inc

    return output_


def part1(data: list) -> list:
    """
    >>> execute([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99])
    [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    >>> out = execute([1102,34915192,34915192,7,4,7,99,0])
    >>> len(str(out[0]))
    16
    >>> execute([104,1125899906842624,99])[0]
    1125899906842624
    """
    return execute(data, input_=1)[0]


def part2(data: list) -> int:

    return execute(data, input_=2)[0]


if __name__ == "__main__":
    import doctest
    import sys
    doctest.testmod(verbose=True)

    if (arg := sys.argv[1]) != 'test':

        parts = {'1': part1, '2': part2}
        try:
            func = parts[arg]
        except IndexError:
            print("Which part?")

        print(func(get_data()))
