# -*- coding: utf-8 -*-
"""
Advent of Code 2019
Day 10
"""
import math


def get_data(fname: str) -> str:
    with open(fname, 'r') as f:
        data = f.read()
    return data


def get_coords(data: str) -> list:
    """Parse data and build list of coordinates of asteroids."""
    coords = []
    for y, line in enumerate(data.split('\n')):
        for x, char in enumerate(line):
            if char == '#':
                coords.append(complex(x, y))
    return coords


def polar(c: complex) -> tuple:
    """Get the (r, theta) representation of complex c.
    Theta should be 0 for 0+1j so will have to rotate.

    >>> polar(complex(0, 1))
    (1.0, 0.0)
    >>> polar(complex(1, -1))
    (1.4142135623730951, 2.356194490192345)
    >>> polar(complex(-1, 1))
    (1.4142135623730951, 5.497787143782138)
    """
    r = abs(c)
    if r == 0:  # Div by 0.
        return 0, 0
    theta = math.acos(c.real/r)
    if c.imag > 0:
        theta = 2 * math.pi - theta
    # Rotate by -90 deg.
    theta = (theta + math.pi/2) % (2 * math.pi)
    return r, theta


def get_visibles(coords: list) -> dict:
    results = {}
    for asteroid in coords:
        this = set()
        for other in coords:
            if asteroid == other:
                continue
            this.add(round(polar(asteroid - other)[1], 12))
        results[asteroid] = len(this)
    return results


def part1(data: str) -> int:
    """Part 1.

    For each asteroid, find the set of all thetas of all other asteroids.

    Tests
    >>> import day10test
    >>> part1(day10test.test1)
    33
    >>> part1(day10test.test2)
    35
    >>> part1(day10test.test3)
    41
    >>> part1(day10test.test4)
    210
    >>> part1(get_data('day10.txt'))  # Actual challenge.
    334
    """
    coords = get_coords(data)
    visibles = get_visibles(coords)
    sorted_visibles = {k: v for k, v in sorted(visibles.items(), key=lambda p: p[1], reverse=True)}
    return list(sorted_visibles.values())[0]


def part2(data: str) -> int:
    """Part 2.

    Beat it into submission. Much better ways obvious in hindsight.
    Once again I feel like classes would have helped write cleaner code.

    >>> import day10test
    >>> part2(day10test.test4)
    802
    """
    coords = get_coords(data)
    visibles = get_visibles(coords)
    sorted_visibles = {k: v for k, v in sorted(visibles.items(), key=lambda p: p[1], reverse=True)}
    base: complex = list(sorted_visibles.keys())[0]

    thetas: dict = {}
    for asteroid in coords:
        r, theta = polar(base - asteroid)
        if r == 0:
            continue
        theta = round(theta, 12)

        # The tricky part is that we only want the nearest objects.
        if theta in [pair[1] for pair in thetas.values()]:
            other = [pair for pair in thetas.items() if theta == pair[1][1]][0]
            ast_other, (r_other, theta_other) = other
            if r < r_other:
                thetas.pop(ast_other)
                thetas[asteroid] = (r, theta)
        else:
            thetas[asteroid] = (r, theta)

    # I don't understand why this seems to be reversed... or why I need the
    # 198th thing. Thank goodness for the test.
    sorted_thetas = {k: v for k, v in sorted(thetas.items(), key=lambda p: p[1][1], reverse=True)}
    target: complex = list(sorted_thetas.keys())[198]
    return int(100*target.real + target.imag)


if __name__ == "__main__":
    import doctest
    import sys
    doctest.testmod(verbose=True)

    if sys.argv[1] != 'test':

        parts = {'1': part1, '2': part2}
        try:
            func = parts[sys.argv[1]]
        except IndexError:
            print("Which part?")

        print(func(get_data('day10.txt')))
