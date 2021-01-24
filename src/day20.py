from dataclasses import dataclass
from typing import List, Tuple


def read_input() -> List[str]:
    with open("../input/day20.txt") as file:
        return file.readlines()


Coord = Tuple[int, ...]
Particle = Tuple[Coord, Coord, Coord]


@dataclass
class Particle:
    pos: Coord
    vel: Coord
    acc: Coord

    def move(self) -> Coord:
        self.vel = tuple(map(sum, zip(self.vel, self.acc)))
        self.pos = tuple(map(sum, zip(self.pos, self.vel)))
        return self.pos


def parse_input(lines: List[str]) -> List[Particle]:
    return [Particle(*(tuple(map(int, p[3:-1].split(","))) for p in line.strip().split(", "))) for line in lines]


def part1(particles: List[Particle]) -> int:
    return min(range(len(particles)), key=lambda i: sum(map(abs, particles[i].acc)))


def part2(particles: List[Particle]) -> int:
    pos = {p.pos: p for p in particles}
    for i in range(10000):
        new_pos = {}
        dups = set()
        for p in pos.values():
            p.move()
            if p.pos in new_pos and p.pos not in dups:
                dups.add(p.pos)
            else:
                new_pos[p.pos] = p

        for p_pos in dups:
            del new_pos[p_pos]

        pos = new_pos

    return len(pos)


def test_part1_example():
    example = """p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>""".splitlines()
    assert part1(parse_input(example)) == 0


def test_part1():
    print(part1(parse_input(read_input())))


def test_part2_example():
    example="""p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>    
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>""".splitlines()
    assert part2(parse_input(example)) == 1


def test_part2():
    print(part2(parse_input(read_input())))
