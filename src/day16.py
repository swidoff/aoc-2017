import re
from typing import List, Optional, Union


def read_input() -> List[str]:
    with open("../input/day16.txt") as file:
        return file.readline().strip().split(",")


def part1(moves: List[str], chars: Optional[Union[str, int]] = 16) -> str:
    if isinstance(chars, int):
        ls = list(chr(ord("a") + i) for i in range(0, chars))
    else:
        ls = list(chars)

    for move in moves:
        if match := re.match(r"s(\d+)", move):
            amount = int(match.group(1))
            ls = ls[-amount:] + ls[:-amount]
        elif match := re.match(r"x(\d+)/(\d+)", move):
            pos1 = int(match.group(1))
            pos2 = int(match.group(2))
            ls[pos1], ls[pos2] = ls[pos2], ls[pos1]
        elif match := re.match(r"p(\w)/(\w)", move):
            pos1 = ls.index(match.group(1))
            pos2 = ls.index(match.group(2))
            ls[pos1], ls[pos2] = ls[pos2], ls[pos1]

    return "".join(ls)


def part2(moves: List[str], chars: int = 16) -> str:
    ls = "".join(chr(ord("a") + i) for i in range(0, chars))
    seen = []
    while ls not in seen:
        seen.append(ls)
        ls = part1(moves, ls)

    return seen[1_000_000_000 % len(seen)]


example = ["s1", "x3/4", "pe/b"]


def test_part1_example():
    assert part1(example, chars=5) == "baedc"


def test_part1():
    print(part1(read_input()))


def test_part2():
    print(part2(read_input()))
