import os
import math
from collections import deque

filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")
data = [
    [int(i) for i in "9" + line.strip() + "9"] for line in open(filename).readlines()
]
data = [[9] * len(data[0])] + data + [[9] * len(data[0])]
offsets = [[-1, 0], [1, 0], [0, -1], [0, 1]]

lowpoints, basins, visited = 0, [], [[False] * len(data[0]) for _ in range(len(data))]
for row in range(1, len(data) - 1):
    for col in range(1, len(data[0]) - 1):
        lowpoints += (
            data[row][col] + 1
            if data[row][col] < min([data[row + r][col + c] for r, c in offsets])
            else 0
        )
        if data[row][col] < 9 and not visited[row][col]:
            basins.append(0)
            q = deque([(row, col)])
            while q:
                r, c = q.popleft()
                if not visited[r][c]:
                    visited[r][c] = True
                    basins[-1] += 1
                    q.extend(
                        [(r + a, c + b) for a, b in offsets if data[r + a][c + b] < 9]
                    )

print("Part 1:", lowpoints)
print("Part 2:", math.prod(sorted(basins)[-3:]))
# print(math.prod(sorted(basins)))
