import os

filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")


with open(filename) as f:
    content = f.readlines()
content = [list(x.strip()) for x in content]
content = [[int(x) for x in row] for row in content]

step = 0
ways = [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]


def find_nbrs(content, i, j):
    for way in ways:
        x = i + way[0]
        y = j + way[1]
        max = len(content)
        if x < max and y < max and x >= 0 and y >= 0:
            nbr = content[x][y]
            if nbr > 9:
                content[x][y] = 0
                find_nbrs(content, x, y)
            elif nbr == 0:
                continue
            else:
                content[x][y] += 1


for i, row in enumerate(content):
    for j, cell in enumerate(row):
        # find_nbrs(content, i, j)
        # if cell == 9:
        #     continue
        #     # content[i][j] = 0
        #     # find_nbrs(content, i, j)
        # else:
        content[i][j] += 1

step += 1

while (9 in sum(content, [])) or (10 in sum(content, [])):
    for i, row in enumerate(content):
        for j, cell in enumerate(row):
            if cell > 9:
                find_nbrs(content, i, j)

# for i, row in enumerate(content):
#     for j, cell in enumerate(row):
#         if cell == 0:
#             find_nbrs(content, i, j)

print(content)
