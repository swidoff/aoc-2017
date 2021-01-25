import operator
import re
from collections import defaultdict
from typing import List


def read_input() -> List[str]:
    with open("../input/day23.txt") as file:
        return file.readlines()


ops = {
    "sub": operator.sub,
    "mul": operator.mul,
}


def part1(lines: List[str]) -> int:
    registers = defaultdict(lambda: 0)
    registers["a"] = 1
    mul = 0

    def value_of(v: str) -> int:
        return registers[v] if v.isalpha() else int(v)

    pc = 0
    while 0 <= pc < len(lines):
        offset = 1
        line = lines[pc]
        if match := re.match(r"set ([-\w]+) ([-\w]+)", line):
            registers[match.group(1)] = value_of(match.group(2))
        elif match := re.match(r"(sub|mul) ([-\w]+) ([-\w]+)", line):
            lhs, op, rhs = match.group(2), match.group(1), match.group(3)
            registers[lhs] = ops[op](value_of(lhs), value_of(rhs))
            if op == "mul":
                mul += 1
        elif match := re.match(r"jnz ([-\w]+) ([-\w]+)", line):
            if value_of(match.group(1)) != 0:
                offset = value_of(match.group(2))

        pc += offset

    return mul


def is_prime(num: int) -> bool:
    # Iterate from 2 to n / 2
    for i in range(2, num):
        if (num % i) == 0:
            return False

    return True


def part2():
    return sum(not is_prime(i) for i in range(108100, 125101, 17))


def test_part1():
    print(part1(read_input()))


def test_part2():
    print(part2())


# if __name__ == '__main__':
#     part2(read_input())
