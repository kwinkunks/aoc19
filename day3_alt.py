# -*- coding: utf-8 -*-
"""
Advent of Code 2019
Day 3

Alternative solution using complex numbers instead of (x, y) tuple. I can't
believe I forgot about this trick. The only thing it really does is make the
math steps a bit easier, because you can express those as complexes too.
"""


def get_data() -> list:
    with open('day3.txt', 'r') as f:
        return [line.split(',') for line in f.readlines()]


def l1_norm(c: complex) -> int:
    """
    L1 norm.

    Tests
    >>> l1_norm(3+4j) == l1_norm(4-3j)
    True
    """
    return int(abs(c.real) + abs(c.imag))


def get_xings(data: list) -> dict:
    """This is the main routine.
    Make the moves, recording where we have been. Initially in a list
    of tuples.

    Update for Part 2: ...and also store the path length to each point.
    Using a dictionary for this.
    """
    ops = {'U': 0+1j, 'D': 0-1j, 'L': -1+0j, 'R': 1+0j}

    visits0, visits1, xings = {0+0j: 0}, {0+0j: 0}, {}

    for w, wire in enumerate(data):
        pos, dist = 0+0j, 0

        for segment in wire:
            direction, distance = segment[0], int(segment[1:])
            for step in range(distance):
                pos += ops[direction]
                dist += 1
                if w == 0:
                    visits0[pos] = dist
                else:
                    visits1[pos] = dist
                    if pos in visits0:
                        # Store location and distances of the crossing.
                        xings[pos] = l1_norm(pos), visits0[pos] + visits1[pos]
    return xings


def part1(data: list) -> int:
    """Part 1.

    Tests
    >>> part1([['R8','U5','L5','D3'], ['U7','R6','D4','L4']])
    6
    >>> part1([['R75','D30','R83','U83','L12','D49','R71','U7','L72'], ['U62','R66','U55','R34','D71','R55','D58','R83']])
    159
    >>> part1([['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'], ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']])
    135
    """
    xings = get_xings(data)
    return sorted(xings.values())[0][0]


def part2(data: list) -> int:
    """Part 2.

    Tests
    >>> part2([['R8','U5','L5','D3'], ['U7','R6','D4','L4']])
    30
    >>> part2([['R75','D30','R83','U83','L12','D49','R71','U7','L72'], ['U62','R66','U55','R34','D71','R55','D58','R83']])
    610
    >>> part2([['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'], ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']])
    410
    """
    xings = get_xings(data)
    return sorted(xings.values(), key=lambda t: t[1])[0][1]


if __name__ == "__main__":
    import doctest
    import sys
    doctest.testmod(verbose=True)

    if sys.argv[1] != 'test':
        data = get_data()
        parts = {'1': part1(data), '2': part2(data)}
        try:
            print(parts[sys.argv[1]])
        except IndexError:
            print("Which part?")
