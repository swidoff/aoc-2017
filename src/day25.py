from collections import defaultdict
from typing import Dict, List, Tuple

INPUT = {
    "A": [(1, 1, "B"), (0, -1, "C")],
    "B": [(1, -1, "A"), (1, 1, "D")],
    "C": [(0, -1, "B"), (0, -1, "E")],
    "D": [(1, 1, "A"), (0, 1, "B")],
    "E": [(1, -1, "F"), (1, -1, "C")],
    "F": [(1, 1, "D"), (1, 1, "A")],
}


def evaluate(rules: Dict[str, List[Tuple[int, int, str]]], iterations: int = 12481997) -> int:
    tape = defaultdict(lambda: 0)
    state = "A"
    pos = 0

    for _ in range(iterations):
        value, move, next_state = rules[state][tape[pos]]
        tape[pos] = value
        pos += move
        state = next_state

    return sum(tape.values())


def test_part1_example():
    example = {
        "A": [(1, 1, "B"), (0, -1, "B")],
        "B": [(1, -1, "A"), (1, 1, "A")],
    }

    assert evaluate(example, 6) == 3


def test_part1():
    print(evaluate(INPUT))
