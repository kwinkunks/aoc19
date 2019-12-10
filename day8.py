# -*- coding: utf-8 -*-
"""
Advent of Code 2019
Day 8
"""


def get_data() -> list:
    with open('day8.txt', 'r') as f:
        return [int(x) for x in f.read()]


def count_pixels(layer: list) -> dict:
    stats: dict = {}
    for row in layer:
        for item in row:
            stats[item] = stats.get(item, 0) + 1
    return stats


def make_image(data: list, size: tuple) -> list:
    img: list = []
    h: int
    w: int
    L: int
    h, w = size  # Type hints not allowed with simultaneous or implicit assignment.
    for L in range(len(data) // int(size[0] * size[1])):
        img.append([[data[L*h*w + i*w + j] for j in range(size[1])] for i in range(size[0])])
    return img


def part1(data: list) -> int:
    size: tuple = (6, 25)
    stats: list = [count_pixels(layer) for layer in make_image(data, size)]
    fewest_zeros: dict = sorted(stats, key=lambda d: d.get(0, 0))[0]
    return fewest_zeros[1] * fewest_zeros[2]


def flatten(l: list) -> list:
    f = []
    for row in l:
        for i in row:
            f.append(i)
    return f


def get_px(pixels: list) -> int:
    for px in pixels:
        if px == 2: continue
        return px
    return -1


def visualize(img: list) -> str:
    colours = [' ', '\u2588']
    s = ''
    for row in img:
        for px in row:
            s += colours[px]
        s += '\n'
    return s


def decode(img: list) -> list:
    """Part 2.
    """
    h, w = len(img[0]), len(img[0][0])
    out = [[-1]*w for x in range(h)]
    for r, c in zip(flatten([[x]*w for x in range(h)]), h*list(range(25))):
        out[r][c] = get_px([layer[r][c] for layer in img])
    return out


def part2(data: list) -> str:
    """Part 2.
    """
    size: tuple = (6, 25)
    img = decode(make_image(data, size))
    return visualize(img)


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
