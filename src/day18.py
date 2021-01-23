import operator
import re
from collections import defaultdict, deque
from typing import List, Iterator, Deque

import toolz


def read_input() -> List[str]:
    with open("../input/day18.txt") as file:
        return file.readlines()


ops = {
    "add": operator.add,
    "mul": operator.mul,
    "mod": operator.mod,
}


def evaluate(lines: List[str]) -> Iterator[int]:
    registers = defaultdict(lambda: 0)
    last_played = None

    def value_of(v: str) -> int:
        return registers[v] if v.isalpha() else int(v)

    pc = 0
    while 0 <= pc < len(lines):
        offset = 1
        line = lines[pc]
        if match := re.match(r"snd ([-\w]+)", line):
            last_played = value_of(match.group(1))
        elif match := re.match(r"set ([-\w]+) ([-\w]+)", line):
            registers[match.group(1)] = value_of(match.group(2))
        elif match := re.match(r"(add|mul|mod) ([-\w]+) ([-\w]+)", line):
            lhs, op, rhs = match.group(2), match.group(1), match.group(3)
            registers[lhs] = ops[op](value_of(lhs), value_of(rhs))
        elif match := re.match(r"rcv ([-\w]+)", line):
            if value_of(match.group(1)):
                yield last_played
        elif match := re.match(r"jgz ([-\w]+) ([-\w]+)", line):
            if value_of(match.group(1)) > 0:
                offset = value_of(match.group(2))

        pc += offset


def part1(lines: List[str]) -> int:
    return toolz.first(v for v in evaluate(lines) if v != 0)


class Program(object):
    def __init__(self, lines: List[str], p: int, in_q: Deque[int], out_q: Deque[int]):
        self.lines = lines
        self.reg = defaultdict(lambda: 0)
        self.reg["p"] = p
        self.in_q = in_q
        self.out_q = out_q
        self.pc = 0
        self.sends = 0

    def evaluate(self) -> int:
        def value_of(v: str) -> int:
            return self.reg[v] if v.isalpha() else int(v)

        count = 0
        while 0 <= self.pc < len(self.lines):
            offset = 1
            line = self.lines[self.pc]
            if match := re.match(r"snd ([-\w]+)", line):
                self.out_q.append(value_of(match.group(1)))
                self.sends += 1
            elif match := re.match(r"set ([-\w]+) ([-\w]+)", line):
                self.reg[match.group(1)] = value_of(match.group(2))
            elif match := re.match(r"(add|mul|mod) ([-\w]+) ([-\w]+)", line):
                lhs, op, rhs = match.group(2), match.group(1), match.group(3)
                self.reg[lhs] = ops[op](value_of(lhs), value_of(rhs))
            elif match := re.match(r"rcv ([-\w]+)", line):
                if self.in_q:
                    self.reg[match.group(1)] = self.in_q.popleft()
                else:
                    break
            elif match := re.match(r"jgz ([-\w]+) ([-\w]+)", line):
                if value_of(match.group(1)) > 0:
                    offset = value_of(match.group(2))

            count += 1
            self.pc += offset

        return count


def part2(lines: List[str]) -> int:
    q1 = deque()
    q2 = deque()
    p0 = Program(lines, 0, q1, q2)
    p1 = Program(lines, 1, q2, q1)

    progress0, progress1 = 1, 1
    while progress0 or progress1:
        progress0 = p0.evaluate()
        progress1 = p1.evaluate()

    return p1.sends


def test_part1_example():
    example = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2""".splitlines()
    assert part1(example) == 4


def test_part1():
    print(part1(read_input()))


def test_part2_example():
    example = """snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d""".splitlines()
    assert part2(example) == 3


def test_part2():
    print(part2(read_input()))
