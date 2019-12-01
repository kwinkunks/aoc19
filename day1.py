# -*- coding: utf-8 -*-
"""
Advent of Code 2019
Day 1

Started off using map, but switched to list comps b/c I can never remember
to only traverse the map once.
"""


def get_data() -> list:
    with open('day1.txt', 'r') as f:
        return [float(x) for x in f.readlines()]


def part1(data: list) -> int:
    """Part 1. Floor... we can use int().

    Tests
    >>> part1([12])
    2
    >>> part1([14])
    2
    >>> part1([1969])
    654
    >>> part1([100756])
    33583
    """
    return sum(int(x/3) - 2 for x in data)


def sum_fuel(fuel: int) -> int:
    """Recursively sum the fuel.
    """
    new = int(fuel/3) - 2
    if new < 1:
        return 0
    else:
        return new + sum_fuel(new)


def part2(data: list) -> int:
    """Part 2. Crying out for recursion.

    Tests
    >>> part2([14])
    2
    >>> part2([1969])
    966
    >>> part2([100756])
    50346
    """
    results = [int(x/3) - 2 for x in data]
    extras = [sum_fuel(r) for r in results]
    return sum(extras) + sum(results)


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
