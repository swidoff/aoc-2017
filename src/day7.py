import re
from typing import List, Tuple, Optional

import toolz


def read_input() -> List[str]:
    with open("../input/day7.txt") as file:
        return file.readlines()


Row = Tuple[str, int, Tuple[str, ...]]


def parse_input(lines: List[str]) -> List[Row]:
    return [
        (match.group(1), int(match.group(2)), tuple(match.group(3)[4:].split(", ")) if match.group(3) else tuple())
        for line in lines
        if (match := re.match(r"(\w+) \((\d+)\)( -> [, \w]+)?", line)) is not None
    ]


def part1(rows: List[Row]) -> str:
    return toolz.first((row for row in rows if all(row[0] not in other_row[2] for other_row in rows)))[0]


def part2(rows: List[Row]) -> int:
    row_by_id = {row[0]: row for row in rows}
    bottom_row = row_by_id[part1(rows)]
    weights = {}

    def fill_weights(row: Row) -> int:
        weight = row[1] + sum(fill_weights(row_by_id[r]) for r in row[2])
        weights[row[0]] = weight
        return weight

    def solve(row: Row) -> Optional[int]:
        for r in row[2]:
            if (res := solve(row_by_id[r])) is not None:
                return res

        res = None
        child_weights = sorted([(weights[r], r) for r in row[2]], key=lambda k: k[0])
        if child_weights:
            if child_weights[0][0] != child_weights[1][0]:
                r_small = child_weights[0][1]
                w_diff = child_weights[0][0] - child_weights[1][0]
                res = row_by_id[r_small][1] + w_diff
            elif child_weights[-2][0] != child_weights[-1][0]:
                r_big = child_weights[-1][1]
                w_diff = child_weights[-1][0] - child_weights[-2][0]
                res = row_by_id[r_big][1] - w_diff

        return res

    fill_weights(bottom_row)
    return solve(bottom_row)


example = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)""".splitlines()


def test_part1_example():
    assert part1(parse_input(example)) == "tknk"


def test_part1():
    print(part1(parse_input(read_input())))


def test_part2_example():
    assert part2(parse_input(example)) == 60


def test_part2():
    print(part2(parse_input(read_input())))
