def part1(steps: int):
    ls = [0]
    pos = 0
    for i in range(1, 2017 + 1):
        pos = (pos + steps) % len(ls) + 1
        ls.insert(pos, i)

    return ls[(pos + 1) % len(ls)]


def part2(steps: int, iters: int = 50_000_000):
    pos = 0
    zero_pos = 0
    next_value = -1
    for i in range(1, iters + 1):
        pos = (pos + steps) % i + 1
        if pos == zero_pos:
            zero_pos = pos
        elif pos == zero_pos + 1:
            next_value = i

    return next_value


def test_part1_example():
    assert part1(3) == 638


def test_part1():
    assert part1(376) == 777


def test_part2():
    print(part2(376))
