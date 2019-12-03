# -*- coding: utf-8 -*-
"""
Advent of Code 2019
Day 3
"""


def get_data() -> list:
    with open('day3.txt', 'r') as f:
        return [line.split(',') for line in f.readlines()]


def get_xings(data: list) -> dict:
    """This is the main routine.
    Make the moves, recording where we have been. Initially in a list
    of tuples.

    Update for Part 2: ...and also store the path length to each point.
    Using a dictionary for this.
    """
    visits0, visits1, xings = {(0, 0): 0}, {(0, 0): 0}, {}

    for w, wire in enumerate(data):
        x, y = 0, 0
        dist = 0

        for segment in wire:
            direction, distance = segment[0], int(segment[1:])
            for step in range(distance):
                if direction == 'U':
                    y += 1
                elif direction == 'D':
                    y -= 1
                elif direction == 'L':
                    x -= 1
                elif direction == 'R':
                    x += 1
                dist += 1
                if w == 0:
                    visits0[(x, y)] = dist
                else:
                    visits1[(x, y)] = dist
                    if (x, y) in visits0:
                        # Store llocation and distances of the crossing.
                        xings[(x, y)] = abs(x) + abs(y), visits0[(x, y)] + visits1[(x, y)]
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
