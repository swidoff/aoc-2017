import math
from collections import defaultdict
from typing import List, Dict, Tuple


def read_input() -> List[str]:
    with open("../input/day22.txt") as file:
        return file.readlines()


def parse_grid(lines: List[str]) -> Dict[Tuple[int, int], str]:
    grid = defaultdict(lambda: ".")
    grid.update(((r, c), ch) for r, row in enumerate(lines) for c, ch in enumerate(row.strip()))
    return grid


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def part1(grid: Dict[Tuple[int, int], str]) -> int:
    size = int(math.sqrt(len(grid)))
    r = size // 2
    c = r
    infections = 0
    dir_idx = 0

    for _ in range(10000):
        if grid[(r, c)] == "#":
            turn = 1
            grid[(r, c)] = "."
        else:
            turn = -1
            grid[(r, c)] = "#"
            infections += 1

        dir_idx = (dir_idx + turn) % 4
        r += directions[dir_idx][0]
        c += directions[dir_idx][1]

    return infections

def part2(grid: Dict[Tuple[int, int], str], iterations: int = 10_000_000) -> int:
    size = int(math.sqrt(len(grid)))
    r = size // 2
    c = r
    infections = 0
    dir_idx = 0

    for _ in range(iterations):
        ch = grid[(r, c)]
        if ch == "#":
            turn = 1
            new_ch = "F"
        elif ch == ".":
            turn = -1
            new_ch = "W"
        elif ch == "W":
            turn = 0
            new_ch = "#"
            infections += 1
        else:
            turn = 2
            new_ch = "."

        grid[(r, c)] = new_ch
        dir_idx = (dir_idx + turn) % 4
        r += directions[dir_idx][0]
        c += directions[dir_idx][1]

    return infections


def test_part1_example():
    example = """..#
#..
...""".splitlines()
    assert part1(parse_grid(example)) == 5587


def test_part1():
    print(part1(parse_grid(read_input())))


def test_part2_example():
    example = """..#
#..
...""".splitlines()
    assert part2(parse_grid(example), 100) == 26
    assert part2(parse_grid(example)) == 2511944


def test_part2():
    print(part2(parse_grid(read_input())))
