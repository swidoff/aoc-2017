from typing import List, Tuple


def read_input() -> List[int]:
    with open("../input/day6.txt") as file:
        return list(map(int, file.readline().strip().split("\t")))


def allocate(initial: List[int]) -> Tuple[int, int]:
    seen = {}
    steps = 0
    state = tuple(initial)
    while state not in seen:
        seen[state] = steps

        i, v = max(enumerate(state), key=lambda s: s[1])

        new_state = list(state)
        new_state[i] = 0
        for j in range(1, v + 1):
            target = (i + j) % len(new_state)
            new_state[target] += 1

        state = tuple(new_state)
        steps += 1

    return steps, steps - seen[state]


def part1(initial: List[int]) -> int:
    return allocate(initial)[0]


def part2(initial: List[int]) -> int:
    return allocate(initial)[1]


def test_part1_example():
    assert part1([0, 2, 7, 0]) == 5


def test_part1():
    print(part1(read_input()))


def test_part2_example():
    assert part2([0, 2, 7, 0]) == 4


def test_part2():
    print(part2(read_input()))
