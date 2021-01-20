import operator
import re
from collections import defaultdict
from typing import List, Iterator

import toolz


def read_input() -> List[str]:
    with open("../input/day8.txt") as file:
        return file.readlines()


COND_MAP = {
    "==": operator.eq,
    "!=": operator.ne,
    ">": operator.gt,
    ">=": operator.ge,
    "<": operator.lt,
    "<=": operator.le,
}

OP_MAP = {
    "inc": operator.add,
    "dec": operator.sub,
}


def execute(lines: List[str]) -> Iterator[int]:
    registers = defaultdict(lambda: 0)

    for line in lines:
        match = re.match(r"(\w+) (inc|dec) (-?[\d]+) if (\w+) ([<>=!]+) (-?[\d]+)", line)
        reg1 = match.group(1)
        op = match.group(2)
        amount = int(match.group(3))
        reg2 = match.group(4)
        cond = match.group(5)
        threshold = int(match.group(6))
        if COND_MAP[cond](registers[reg2], threshold):
            registers[reg1] = OP_MAP[op](registers[reg1], amount)
            yield max(registers.values())


def part1(lines: List[str]) -> int:
    return toolz.last(execute(lines))


def part2(lines: List[str]) -> int:
    return max(execute(lines))


example = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10""".splitlines()


def test_part1_example():
    assert part1(example) == 1


def test_part1():
    print(part1(read_input()))


def test_part2_example():
    assert part2(example) == 10


def test_part2():
    print(part2(read_input()))
