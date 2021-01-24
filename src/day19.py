from typing import List, Tuple


def read_input() -> List[str]:
    with open("../input/day19.txt") as file:
        return file.readlines()


def solve(lines: List[str]) -> Tuple[str, int]:
    grid = [[c for c in line] for line in lines]

    row = 0
    col = grid[0].index("|")
    c = grid[row][col]
    dr, dc = 1, 0
    res = []
    steps = 0
    while c != " ":
        if c.isalpha():
            res.append(c)
        elif c == "+":
            for dr_new, dc_new in {(1, 0), (0, 1), (-1, 0), (0, -1)} - {(-dr, -dc)}:
                new_r, new_c = row + dr_new, col + dc_new
                if 0 <= new_r < len(lines) and 0 <= new_c < len(lines[new_r]) and lines[new_r][new_c] != " ":
                    dr, dc = dr_new, dc_new
                    break

        row += dr
        col += dc
        c = grid[row][col]
        steps += 1

    return "".join(res), steps


def test_example():
    example = """     
     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ 
""".splitlines()[
        1:
    ]
    res = solve(example)
    assert res[0] == "ABCDEF"
    assert res[1] == 38


def test_for_reals():
    print(solve(read_input()))
