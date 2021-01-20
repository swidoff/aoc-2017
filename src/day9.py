from typing import Tuple


def read_input() -> str:
    with open("../input/day9.txt") as file:
        return file.readline().strip()


def solve(line: str) -> Tuple[int, int]:
    q = []
    score = 0
    count = 0

    for c in line:
        if q:
            qc = q[-1]
            if qc == "!":
                q.pop()
            elif qc == "<":
                if c == ">":
                    q.pop()
                elif c == "!":
                    q.append(c)
                else:
                    count += 1
            elif qc == "{" and c == "}":
                score += len(q)
                q.pop()
            elif c != ',':
                q.append(c)
        else:
            q.append(c)

    return score, count


def part1(line: str) -> int:
    return solve(line)[0]


def part2(line: str) -> int:
    return solve(line)[1]


def test_part1_examples():
    assert part1("{}") == 1
    assert part1("{{{}}}") == 6
    assert part1("{{},{}}") == 5
    assert part1("{{{},{},{{}}}}") == 16
    assert part1("{<a>,<a>,<a>,<a>}") == 1
    assert part1("{{<ab>},{<ab>},{<ab>},{<ab>}}") == 9
    assert part1("{{<!!>},{<!!>},{<!!>},{<!!>}}") == 9
    assert part1("{{<a!>},{<a!>},{<a!>},{<ab>}}") == 3


def test_part1():
    print(part1(read_input()))


def test_part2_examples():
    assert part2("<>") == 0
    assert part2("<random characters>") == 17
    assert part2("<<<<>") == 3
    assert part2("<{!>}>") == 2
    assert part2("<!!>") == 0
    assert part2("<!!!>>") == 0
    assert part2("<{o\"i!a,<{i<a>") == 10


def test_part2():
    print(part2(read_input()))
