from typing import List


def read_input() -> List[str]:
    with open("../input/day5.txt") as file:
        return file.readlines()


def parse_input(lines: List[str]) -> List[int]:
    return list(map(int, lines))


def part1(ls: List[int]) -> int:
    steps = 0
    i = 0
    while i < len(ls):
        new_i = i + ls[i]
        ls[i] += 1
        steps += 1
        i = new_i

    return steps


def part2(ls: List[int]) -> int:
    steps = 0
    i = 0
    while i < len(ls):
        new_i = i + ls[i]
        ls[i] += 1 if ls[i] < 3 else -1
        steps += 1
        i = new_i

    return steps


def test_part1_example():
    assert part1([0, 3, 0, 1, -3]) == 5


def test_part1():
    print(part1(parse_input(read_input())))


def test_part2_example():
    assert part2([0, 3, 0, 1, -3]) == 10


def test_part2():
    print(part2(parse_input(read_input())))
