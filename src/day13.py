from typing import List, Dict

import toolz


def read_input() -> List[str]:
    with open("../input/day13.txt") as file:
        return file.readlines()


def parse_input(lines: List[str]) -> Dict[int, int]:
    res = {}
    for line in lines:
        key, value = map(int, line.split(": "))
        res[key] = value

    return res


def part1(wall: Dict[int, int]) -> int:
    score = 0
    max_depth = max(wall.keys())
    for t in range(max_depth + 1):
        if t in wall:
            pos = t % ((wall[t] - 1) * 2)
            if pos == 0:
                score += t * wall[t]
        t += 1

    return score


def part2(wall: Dict[int, int]) -> int:
    max_depth = max(wall.keys())

    def is_caught(delay: int) -> bool:
        for d in range(max_depth + 1):
            if d in wall:
                pos = (d + delay) % ((wall[d] - 1) * 2)
                if pos == 0:
                    return True
            d += 1
        return False

    return toolz.first(t for t in range(10000000) if not is_caught(t))


example = """0: 3
1: 2
4: 4
6: 4"""


def test_part1_example():
    assert part1(parse_input(example.splitlines())) == 24


def test_part1():
    print(part1(parse_input(read_input())))


def test_part2_example():
    assert part2(parse_input(example.splitlines())) == 10


def test_part2():
    print(part2(parse_input(read_input())))
