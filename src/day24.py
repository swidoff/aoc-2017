import operator
import re
from collections import defaultdict
from typing import List, Tuple, Set

import toolz


def read_input() -> List[str]:
    with open("../input/day24.txt") as file:
        return file.readlines()


def parse_input(lines: List[str]) -> List[Tuple[int, ...]]:
    return [tuple(map(int, line.split("/"))) for line in lines]


def part1(components: List[Tuple[int, ...]]) -> int:
    remaining = set(components)

    def do_it(port: int, strength: int) -> int:
        max_res = strength
        for c in list(remaining):
            if port in c:
                remaining.remove(c)
                other_port = c[1] if c[0] == port else c[0]
                new_str = do_it(other_port, strength + sum(c))
                max_res = max(max_res, new_str)
                remaining.add(c)
        return max_res

    return do_it(0, 0)


def part2(components: List[Tuple[int, ...]]) -> int:
    remaining = set(components)

    def do_it(port: int, length: int, strength: int) -> Tuple[int, int]:
        max_len = length
        max_str = strength
        for c in list(remaining):
            if port in c:
                remaining.remove(c)
                other_port = c[1] if c[0] == port else c[0]
                new_len, new_str = do_it(other_port, length + 1, strength + sum(c))
                if new_len > max_len or (new_len == max_len and new_str > max_str):
                    max_len = new_len
                    max_str = new_str
                remaining.add(c)
        return max_len, max_str

    return do_it(0, 0, 0)[1]


def test_part1_example():
    example = """0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10""".splitlines()
    assert part1(parse_input(example)) == 31


def test_part1():
    print(part1(parse_input(read_input())))


def test_part2():
    print(part2(parse_input(read_input())))
