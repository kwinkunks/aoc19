# -*- coding: utf-8 -*-
"""
Advent of Code 2019
Day 4
"""


def is_monotonic(n: int) -> bool:
    """
    Does not decrease from left to right.

    Tests
    >>> is_monotonic(111111)
    True
    >>> is_monotonic(123435)
    False
    >>> is_monotonic(135669)
    True
    """
    return int(''.join(sorted(str(n)))) - n == 0


def doubles(n: int) -> list:
    return [1 - bool(int(x) - int(y)) for x, y in zip(str(10*n)[1:], str(n))]


def has_double(n: int) -> bool:
    """
    Has 2 adjacent digits the same.

    Tests
    >>> has_double(111111)
    True
    >>> has_double(123435)
    False
    >>> has_double(135669)
    True
    """
    return any(doubles(n))


def has_one_double(n: int) -> bool:
    """
    Has 2 adjacent digits the same.

    Tests
    >>> has_one_double(112233)
    True
    >>> has_one_double(123444)
    False
    >>> has_one_double(111122)
    True
    """
    d = ''.join([str(x) for x in doubles(n)])
    return (d[:2] == '10') or (d[-2:] == '01') or ('010' in d)


def meets_criteria_part1(n: int) -> bool:
    """
    Has it all.

    Tests
    >>> meets_criteria_part1(111111)
    True
    >>> meets_criteria_part1(223450)
    False
    >>> meets_criteria_part1(123789)
    False
    """
    return has_double(n) and is_monotonic(n)


def meets_criteria_part2(n: int) -> bool:
    """
    Has it all for part 2.

    Tests
    >>> meets_criteria_part2(112233)
    True
    >>> meets_criteria_part2(123444)
    False
    >>> meets_criteria_part2(111122)
    True
    """
    return meets_criteria_part1(n) and has_one_double(n)


def part1() -> int:
    """Part 1.
    """
    cands = [n for n in range(108457, 562041 + 1) if meets_criteria_part1(n)]
    return len(cands)


def part2() -> int:
    """Part 2.
    """
    cands = [n for n in range(108457, 562041 + 1) if meets_criteria_part2(n)]
    return len(cands)


if __name__ == "__main__":
    import doctest
    import sys
    doctest.testmod(verbose=True)

    if sys.argv[1] != 'test':

        parts = {'1': part1, '2': part2}
        try:
            print(parts[sys.argv[1]]())
        except IndexError:
            print("Which part?")
