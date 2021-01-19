from collections import defaultdict
from typing import Tuple, Iterator

import toolz

directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def coords() -> Iterator[Tuple[int, int]]:
    r, c = 0, 0
    r_max, c_max, r_min, c_min = 0, 0, 0, 0
    direction = 0
    rd, cd = directions[direction]
    yield r, c

    while True:
        r += rd
        c += cd
        yield r, c

        if not (r_min <= r <= r_max) or not (c_min <= c <= c_max):
            direction = (direction + 1) % 4
            rd, cd = directions[direction]

        r_max = max(r, r_max)
        r_min = min(r, r_min)
        c_max = max(c, c_max)
        c_min = min(c, c_min)


def part1(square: int) -> int:
    r, c = toolz.nth(square - 1, coords())
    return abs(r) + abs(c)


def sums() -> Iterator[int]:
    res = defaultdict(lambda: 0)
    neighbors = [(r, c) for r in range(-1, 2) for c in range(-1, 2)]

    for r, c in coords():
        s = max(sum(res[(r + rd, c + cd)] for rd, cd in neighbors), 1)
        res[(r, c)] = s
        yield s


def part2(square: int) -> int:
    return toolz.first(filter(lambda v: v > square, sums()))


def test_part1_examples():
    assert part1(1) == 0
    assert part1(12) == 3
    assert part1(23) == 2
    assert part1(1024) == 31


def test_part1():
    assert part1(325489) == 552


def test_part2_examples():
    assert toolz.nth(0, sums()) == 1
    assert toolz.nth(1, sums()) == 1
    assert toolz.nth(2, sums()) == 2
    assert toolz.nth(3, sums()) == 4
    assert toolz.nth(4, sums()) == 5


def test_part2():
    print(part2(325489))
