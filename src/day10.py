import operator
from functools import reduce
from typing import List, Tuple

import toolz


def read_input() -> str:
    with open("../input/day10.txt") as file:
        return file.readline().strip()


def parse_input(line: str) -> List[int]:
    return list(map(int, line.split(",")))


def knot_round(ls: List[int], lengths: List[int], pos: int = 0, skip: int = 0) -> Tuple[List[int], int, int]:
    for ln in lengths:
        sublist = [ls[(pos + i) % len(ls)] for i in range(ln)]

        reversed_sublist = list(reversed(sublist))

        for i in range(ln):
            ls[(pos + i) % len(ls)] = reversed_sublist[i]

        pos = (pos + ln) % len(ls) + skip
        skip += 1

    return ls, pos, skip


def part1(ls: List[int], lengths: List[int]) -> int:
    res, *_ = knot_round(ls, lengths)
    return res[0] * res[1]


def to_hex(v: int) -> str:
    s = hex(v)[2:]
    return s if len(s) == 2 else "0" + s


def knot_hash(inp: str) -> str:
    ls = list(range(256))
    new_lengths = [ord(c) for c in inp] + [17, 31, 73, 47, 23]
    pos, skip = 0, 0
    for _ in range(64):
        ls, pos, skip = knot_round(ls, new_lengths, pos, skip)
    res = "".join(to_hex(reduce(operator.xor, part)) for part in toolz.partition(16, ls))
    return res


def part2(inp: str) -> str:
    return knot_hash(inp)


def test_part1_example():
    assert part1(list(range(5)), [3, 4, 1, 5]) == 12


def test_part1():
    print(part1(list(range(256)), parse_input(read_input())))


def test_part2():
    assert knot_hash(read_input()) == "d067d3f14d07e09c2e7308c3926605c4"
