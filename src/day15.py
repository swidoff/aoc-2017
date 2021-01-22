from typing import Iterator

import toolz


def generator(factor: int, start: int, multiple: int) -> Iterator[int]:
    value = start
    while True:
        value = (value * factor) % 2147483647
        if value % multiple == 0:
            yield value


def part1(a_start: int, b_start: int, pairs: int, a_multiple: int = 1, b_multiple: int = 1) -> int:
    a_generator = generator(16807, a_start, a_multiple)
    b_generator = generator(48271, b_start, b_multiple)
    return sum(
        (a_value & 0xFFFF) == (b_value & 0xFFFF)
        for a_value, b_value in toolz.take(pairs, zip(a_generator, b_generator))
    )


def test_part1_example():
    assert part1(65, 8921, pairs=5) == 1
    assert part1(65, 8921, pairs=40_000_000) == 588


def test_part1():
    print(part1(116, 299, pairs=40_000_000))


def test_part2_example():
    assert part1(65, 8921, pairs=5_000_000, a_multiple=4, b_multiple=8) == 309


def test_part2():
    print(part1(116, 299, pairs=5_000_000, a_multiple=4, b_multiple=8))
