from collections import deque
from typing import Iterator, Tuple

import toolz

from day10 import knot_hash


def coords(inp: str) -> Iterator[Tuple[int, int]]:
    for row in range(128):
        key = f"{inp}-{row}"
        hash_hex = knot_hash(key)
        hash_bin = bin(int(hash_hex, base=16))[2:]
        for col, c in enumerate(hash_bin, start=128 - len(hash_bin)):
            if c == "1":
                yield row, col


def part1(inp: str) -> int:
    return toolz.count(coords(inp))


def part2(inp: str) -> int:
    res = 0
    q = deque()
    remaining = set(coords(inp))
    while remaining:
        start = toolz.first(remaining)
        # start = (0, 0)
        q.append(start)
        remaining.remove(start)

        while q:
            r, c = q.popleft()
            for rd, cd in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                coord = (r + rd, c + cd)
                if coord in remaining:
                    q.append(coord)
                    remaining.remove(coord)
        res += 1

    return res


def print_grid(inp: str):
    ones = set(coords(inp))
    for r in range(128):
        line = "".join("#" if (r, c) in ones else "." for c in range(128))
        print(line)


def test_part1_example():
    assert part1("flqrgnkx") == 8108


def test_part1():
    print(part1("uugsqrei"))


def test_part2_example():
    # print()
    # print_grid("flqrgnkx")
    assert part2("flqrgnkx") == 1242


def test_part2():
    print(part2("uugsqrei"))
