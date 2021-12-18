import os

filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")


with open(filename) as f:
    content = f.readlines()
content = [list(x.strip()) for x in content]
content = [[int(x) for x in row] for row in content]

# print(content)
sum_min = 0

indexes = []

for i, row in enumerate(content):
    for j, cell in enumerate(row):
        if j - 1 >= 0:
            left = content[i][j - 1]
        else:
            left = 9
        try:
            right = content[i][j + 1]
        except IndexError:
            right = 9
        try:
            bottom = content[i + 1][j]
        except IndexError:
            bottom = 9
        if i - 1 >= 0:
            top = content[i - 1][j]
        else:
            top = 9
        minimum = []
        minimum.append(left)
        minimum.append(top)
        minimum.append(right)
        minimum.append(bottom)

        # minimum.append(cell)

        if min(minimum) > cell:
            sum_min += cell + 1
            indexes.append((i, j))

print(sum_min)
# print(indexes)


def find_basin(size, i, j, arr):

    arr.append((i, j))
    # print(i, j, content[i][j])

    if (
        (content[i][j - 1] - content[i][j] in [0, 1])
        and (j - 1 >= 0)
        and (content[i][j - 1] != 9)
        and ((i, j - 1) not in arr)
    ):
        size += find_basin(size, i, j - 1, arr)

    if j + 1 < len(content[0]):
        if (
            (content[i][j + 1] - content[i][j] in [0, 1])
            and (content[i][j + 1] != 9)
            and ((i, j + 1) not in arr)
        ):
            size += find_basin(size, i, j + 1, arr)

    if i + 1 < len(content):
        if (
            (content[i + 1][j] - content[i][j] in [0, 1])
            and (content[i + 1][j] != 9)
            and ((i + 1, j) not in arr)
        ):
            size += find_basin(size, i + 1, j, arr)

    if (
        (content[i - 1][j] - content[i][j] in [0, 1])
        and (i - 1 >= 0)
        and (content[i - 1][j] != 9)
        and ((i - 1, j) not in arr)
    ):
        size += find_basin(size, i - 1, j, arr)

    if (
        (content[i - 1][j - 1] - content[i][j] in [0, 1])
        and (i - 1 >= 0)
        and (j - 1 >= 0)
        and (content[i - 1][j - 1] != 9)
        and ((i - 1, j - 1) not in arr)
    ):
        size += find_basin(size, i - 1, j - 1, arr)

    if j + 1 < len(content[0]):
        if (
            (content[i - 1][j + 1] - content[i][j] in [0, 1])
            and (i - 1 >= 0)
            and (content[i - 1][j + 1] != 9)
            and ((i - 1, j + 1) not in arr)
        ):
            size += find_basin(size, i - 1, j + 1, arr)

    if (i + 1 < len(content)) and (j + 1 < len(content[0])):
        if (
            (content[i + 1][j + 1] - content[i][j] in [0, 1])
            and (content[i + 1][j + 1] != 9)
            and ((i + 1, j + 1) not in arr)
        ):
            size += find_basin(size, i + 1, j + 1, arr)

    if i + 1 < len(content):
        if (
            (content[i + 1][j - 1] - content[i][j] in [0, 1])
            and (content[i + 1][j - 1] != 9)
            and ((i + 1, j - 1) not in arr)
        ):
            size += find_basin(size, i + 1, j - 1, arr)

    return size + 1


size_list = []

for ind in indexes:
    size = 1
    val = content[ind[0]][ind[1]]

    i = ind[0]
    j = ind[1]

    arr = []

    size = find_basin(size, i, j, arr)

    size_list.append(len(set(arr)))

multiply = 1

size_list.sort()
print(size_list)

for s in size_list[-3:]:
    multiply *= s

print(multiply)
