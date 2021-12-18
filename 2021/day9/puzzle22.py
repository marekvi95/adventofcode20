import os
from collections import defaultdict


filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")


with open(filename) as f:
    content = f.readlines()
content = [list(x.strip()) for x in content]
content = [[int(x) for x in row] for row in content]

print(content)
indexes = defaultdict(list)

for i, row in enumerate(content):
    for j, cell in enumerate(row):
        indexes[cell].append((i, j))

# print(indexes)

chain = []
x = 0
y = 9

for n in range(1, 10):
    for cord in indexes[n]:
        if (abs(x - cord[0]) + abs(y - cord[1])) == 1:
            chain.append(cord)
        x = cord[0]
        y = cord[1]
    print(indexes[n])

print(chain)
