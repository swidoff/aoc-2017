import operator
from functools import reduce
from typing import List, Tuple, Iterator

import toolz


#   \ n  /
# nw +--+ ne
#   /    \
# -+      +-
#   \    /
# sw +--+ se
#   / s  \
#
# n : (-1, 0, -1)
# ne: (-1, 1, 0)
# se: (0, 1, 1)
# s: (1, 0, 1)
# sw: (1, -1, 0)
# nw: (0, -1, -1)


def read_input() -> List[str]:
    with open("../input/day11.txt") as file:
        return file.readline().strip().split(",")


n = "n"
ne = "ne"
se = "se"
s = "s"
sw = "sw"
nw = "nw"

steps = {
    "n": (-1, 0, -1),
    "ne": (-1, 1, 0),
    "se": (0, 1, 1),
    "s": (1, 0, 1),
    "sw": (1, -1, 0),
    "nw": (0, -1, -1),
}


def walk(dirs) -> Iterator[Tuple[int, int, int]]:
    x, y, z = 0, 0, 0
    for d in dirs:
        xd, yd, zd = steps[d]
        x += xd
        y += yd
        z += zd
        yield x, y, z


def distance(x, y, z):
    return max(abs(x), abs(y), abs(z))


def part1(dirs: List[str]) -> int:
    return distance(*toolz.last(walk(dirs)))


def part2(dirs: List[str]) -> int:
    return max(distance(*coord) for coord in walk(dirs))


def test_part1_examples():
    assert part1([ne, ne, ne]) == 3
    assert part1([ne, ne, sw, sw]) == 0
    assert part1([ne, ne, s, s]) == 2
    assert part1([se, sw, se, sw, sw]) == 3


def test_part1():
    print(part1(read_input()))


def test_part2():
    print(part2(read_input()))
