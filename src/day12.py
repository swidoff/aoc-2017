from collections import deque
from typing import List, Dict, Set

import toolz


def read_input() -> List[str]:
    with open("../input/day12.txt") as file:
        return file.readlines()


def parse_input(lines: List[str]) -> Dict[int, List[int]]:
    res = {}
    for line in lines:
        lhs, rhs = line.split(" <-> ")
        res[int(lhs)] = list(map(int, rhs.split(", ")))

    return res


def group_from(pipes: Dict[int, List[int]], start: int) -> Set[int]:
    seen = set()
    q = deque()
    q.append(start)

    while q:
        for o in pipes[q.popleft()]:
            if o not in seen:
                seen.add(o)
                q.append(o)

    return seen


def part1(pipes: Dict[int, List[int]]) -> int:
    return len(group_from(pipes, 0))


def part2(pipes: Dict[int, List[int]]):
    res = 0
    while pipes:
        start = toolz.first(pipes.keys())
        group = group_from(pipes, start)
        for d in group:
            del pipes[d]
        res += 1

    return res


example = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""


def test_part1_examples():
    assert part1(parse_input(example.splitlines())) == 6


def test_part1():
    print(part1(parse_input(read_input())))


def test_part2_examples():
    assert part2(parse_input(example.splitlines())) == 2


def test_part2():
    print(part2(parse_input(read_input())))
