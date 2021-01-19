from collections import Counter
from typing import List


def read_input() -> List[str]:
    with open("../input/day4.txt") as file:
        return file.readlines()


def is_valid_part1(passphrase: str) -> bool:
    words = passphrase.strip().split(" ")
    distinct_words = set(words)
    return len(distinct_words) == len(words)


def is_valid_part2(passphrase: str) -> bool:
    words = passphrase.strip().split(" ")
    distinct_words = set(tuple(sorted(Counter(word).elements())) for word in words)
    return len(distinct_words) == len(words)


def test_part1():
    print(sum(is_valid_part1(line) for line in read_input()))


def test_part2():
    print(sum(is_valid_part2(line) for line in read_input()))
