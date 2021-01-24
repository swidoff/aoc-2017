from __future__ import annotations

import math
from dataclasses import dataclass
from typing import List, Tuple

import toolz


@dataclass
class Grid(object):
    size: int
    square: List[List[str]]

    def rotate(self) -> Grid:
        square = [[""] * self.size for _ in range(self.size)]
        for r in range(self.size):
            new_c = self.size - r - 1
            for c in range(self.size):
                square[c][new_c] = self.square[r][c]
        return Grid(self.size, square)

    def flip(self) -> Grid:
        square = [[""] * self.size for _ in range(self.size)]
        for r in range(self.size):
            new_r = self.size - r - 1
            for c in range(self.size):
                square[new_r][c] = self.square[r][c]
        return Grid(self.size, square)

    def on(self):
        return sum(c == "#" for row in self.square for c in row)

    def split(self) -> List[Grid]:
        if self.size % 2 == 0:
            size = 2
        else:
            size = 3

        squares = self.size // size
        if squares == 1:
            return [self]

        res = []
        for r in range(squares):
            for c in range(squares):
                square = [row[c * size : c * size + size] for row in self.square[r * size : r * size + size]]
                res.append(Grid(size, square))
        return res

    @staticmethod
    def merge(grids: List[Grid]) -> Grid:
        grids_per_row = int(math.sqrt(len(grids)))
        size = grids_per_row * grids[0].size
        square = [[""] * size for _ in range(size)]
        for i, grid in enumerate(grids):
            big_r = (i // grids_per_row) * grid.size
            big_c = (i % grids_per_row) * grid.size
            for small_r in range(grid.size):
                for small_c in range(grid.size):
                    square[big_r + small_r][big_c + small_c] = grid.square[small_r][small_c]
        return Grid(size, square)

    def print(self):
        for row in self.square:
            print("".join(row))
        print()


@dataclass
class Rule(object):
    pattern: Grid
    replacement: Grid

    def matches(self, grid: Grid):
        if grid.size != self.pattern.size:
            return False
        else:
            for i in range(8):
                if i == 4:
                    grid = grid.flip()
                elif i > 0:
                    grid = grid.rotate()

                if grid.square == self.pattern.square:
                    return True

            return False


def read_input() -> List[str]:
    with open("../input/day21.txt") as file:
        return file.readlines()


def parse_grid(line: str) -> Grid:
    square = [[c for c in row] for row in line.split("/")]
    return Grid(len(square), square)


def parse_input(lines: List[str]) -> List[Rule]:
    res = []
    for line in lines:
        pattern, replacement = line.strip().split(" => ")
        res.append(Rule(parse_grid(pattern), parse_grid(replacement)))
    return res


start = parse_grid(".#./..#/###")


def solve(rules: List[Rule], iterations: int) -> int:
    grid = start
    # print()
    # grid.print()

    for i in range(iterations):
        split_grid = grid.split()
        replacements = [toolz.first(rule.replacement for rule in rules if rule.matches(grid)) for grid in split_grid]
        grid = Grid.merge(replacements)

        # print("Iteration", i)
        # grid.print()

    return grid.on()


def test_part1_example():
    example = """../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#""".splitlines()
    assert solve(parse_input(example), 2) == 12


def test_part1():
    print(solve(parse_input(read_input()), 5))


def test_part2():
    print(solve(parse_input(read_input()), 18))
