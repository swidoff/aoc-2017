import toolz


def read_input() -> str:
    with open("../input/day1.txt") as file:
        return file.readline().strip()


def part1(number: str) -> int:
    return sum(int(d1) for (d1, d2) in toolz.sliding_window(2, number + number[0]) if d1 == d2)


def part2(number: str) -> int:
    step = len(number) // 2
    return sum(int(d1) for i, d1 in enumerate(number) if d1 == number[(i + step) % len(number)])


def test_part1_examples():
    assert part1("1122") == 3
    assert part1("1111") == 4
    assert part1("1234") == 0
    assert part1("91212129") == 9


def test_part1():
    print(part1(read_input()))


def test_part2_examples():
    assert part2("1212") == 6
    assert part2("1221") == 0
    assert part2("123425") == 4
    assert part2("12131415") == 4


def test_part2():
    print(part2(read_input()))
