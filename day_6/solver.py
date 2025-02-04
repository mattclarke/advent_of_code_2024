import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

layout = {}
START = None

for r, l in enumerate(lines):
    for c, ch in enumerate(l):
        if ch == "^":
            START = (r, c)
            layout[r, c] = "."
            continue
        layout[r, c] = ch

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

pos = START
visited = {START}
direction = 0

while True:
    new_pos = (pos[0] + DIRS[direction][0], pos[1] + DIRS[direction][1])
    if new_pos not in layout:
        break
    if layout[new_pos] == ".":
        visited.add(new_pos)
        pos = new_pos
    else:
        direction = (direction + 1) % len(DIRS)

# Part 1 = 4988
print(f"answer = {len(visited)}")

result = 0
for r in range(len(lines)):
    for c in range(len(lines[0])):
        if (r, c) not in visited:
            continue
        visited_2 = {(START, 0)}
        direction = 0
        pos = START
        layout[r, c] = "#"
        while True:
            new_pos = (pos[0] + DIRS[direction][0], pos[1] + DIRS[direction][1])
            if new_pos not in layout:
                break
            if layout[new_pos] == ".":
                if (new_pos, direction) in visited_2:
                    result += 1
                    break
                visited_2.add((new_pos, direction))
                pos = new_pos
            else:
                direction = (direction + 1) % len(DIRS)
        layout[r, c] = "."

# Part 2 = 1697
print(f"answer = {result}")
