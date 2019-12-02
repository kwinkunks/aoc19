# -*- coding: utf-8 -*-
"""
Advent of Code 2019
Day 2
"""


def get_data() -> list:
    with open('day2.txt', 'r') as f:
        data = f.read()
    return [int(x) for x in data.split(',')]


def part1(data: list, noun: int=12, verb: int=2, test: bool=False) -> list:
    """Part 1.

    Tests
    >>> part1([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], test=True)
    [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
    >>> part1([1,0,0,0,99], test=True)
    [2, 0, 0, 0, 99]
    >>> part1([2,3,0,3,99], test=True)
    [2, 3, 0, 6, 99]
    >>> part1([2,4,4,5,99,0], test=True)
    [2, 4, 4, 5, 99, 9801]
    >>> part1([1,1,1,4,99,5,6,0,99], test=True)
    [30, 1, 1, 4, 2, 5, 6, 0, 99]
    """
    # Going to mutate this thing.
    data = data.copy()

    if not test:
        # Restore state, according to question.
        data[1] = noun
        data[2] = verb

    # Well, this is unsatisfying.
    i = 0
    while True:
        op = data[i]
        if op == 99:
            break
        x, y, z = data[i+1:i+4]
        if op == 1:
            data[z] = data[x] + data[y]
        if op == 2:
            data[z] = data[x] * data[y]
        i += 4

    return data


def part2(data: list) -> int:
    """Part 2.

    I have created a monster.
    """
    data = data.copy()

    # Check this still works.
    assert part1(data, noun=12, verb=2)[0] == 5434663

    # Search. Not too many numbers, use brute force. Get new data every time.
    for noun in range(100):
        for verb in range(100):
            result = part1(get_data(), noun=noun, verb=verb)
            if result[0] == 19690720:
                return 100 * noun + verb
    return -1


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    import sys
    data = get_data()
    parts = {'1': part1(data), '2': part2(data)}
    try:
        print(parts[sys.argv[1]])
    except IndexError:
        print("Which part?")
