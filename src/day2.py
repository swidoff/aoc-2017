from typing import List

import toolz


def read_input() -> List[str]:
    with open("../input/day2.txt") as file:
        return file.readlines()


def parse_input(lines: List[str]) -> List[List[int]]:
    def parse_line(line: str) -> List[int]:
        return [int(word) for word in line.split("\t")]

    return [parse_line(line) for line in lines]


def part1(lines: List[List[int]]) -> int:
    return sum(max(line) - min(line) for line in lines)


def part2(lines: List[List[int]]) -> int:
    def find_division(line: List[int]) -> int:
        ls = sorted(line)
        return toolz.first(ls[j] // ls[i] for i in range(len(ls)) for j in range(i + 1, len(ls)) if ls[j] % ls[i] == 0)

    return sum(find_division(line) for line in lines)


def test_part1():
    print(part1(parse_input(read_input())))


def test_part2_example():
    example = """5\t9\t2\t8
9\t4\t7\t3
3\t8\t6\t5
"""
    assert part2(parse_input(example.splitlines())) == 9


def test_part2():
    print(part2(parse_input(read_input())))
