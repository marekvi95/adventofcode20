import os
from collections import Counter
import matplotlib.pyplot as plt


def add_val(start, end, map):
    startx = int(start.split(",")[0])
    starty = int(start.split(",")[1])
    endx = int(end.split(",")[0])
    endy = int(end.split(",")[1])

    if startx == endx:
        if starty < endy:
            nums = range(starty, endy + 1)
        else:
            nums = range(endy, starty + 1)

        for y, val in enumerate(map):
            for x, val in enumerate(val):
                if x in nums:
                    map[x][startx] += 1

    elif starty == endy:
        if startx < endx:
            nums = range(startx, endx + 1)
        else:
            nums = range(endx, startx + 1)

        for y, val in enumerate(map):
            for x, val in enumerate(val):
                if x in nums:
                    map[starty][x] += 1

    else:
        numsx = []
        numsy = []

        for x in range(min(startx, endx), max(startx, endx)):
            numsx.append(int(x))

        for y in range(min(starty, endy), max(starty, endy)):
            numsy.append(int(x))

        for y, val in enumerate(map):
            for x, val in enumerate(val):
                if x in numsy:
                    map[starty][x] += 1
                elif x in numsx:
                    map[x][startx] += 1


def get_indexes(start, end, indexes):
    startx = int(start.split(",")[0])
    starty = int(start.split(",")[1])
    endx = int(end.split(",")[0])
    endy = int(end.split(",")[1])

    if startx == endx:
        if starty < endy:
            nums = range(starty, endy + 1)
        else:
            nums = range(starty, endy - 1, -1)
        # nums = range(min(starty, endy), max(starty+1, endy+1))
        for n in nums:
            indexes.append((startx, n))

    elif starty == endy:
        if startx < endx:
            nums = range(startx, endx + 1)
        else:
            nums = range(startx, endx - 1, -1)
        for n in nums:
            indexes.append((n, starty))

    else:
        if starty < endy:
            numsy = range(starty, endy + 1)
        else:
            numsy = range(starty, endy - 1, -1)
        if startx < endx:
            numsx = range(startx, endx + 1)
        else:
            numsx = range(startx, endx - 1, -1)
        for x in zip(numsx, numsy):
            indexes.append(x)


def calc(m, indexes):
    for y, row in enumerate(m):
        for x, cell in enumerate(row):
            count = indexes.count((x, y))
            m[x][y] = count


if __name__ == "__main__":
    FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")
    data = open(FILE).read().splitlines()

    print(data)

    X = Y = 10

    map = [[0] * X for _ in range(Y)]
    indexes = []

    for r in data:
        splitted = r.split(" -> ")
        start = splitted[0]
        end = splitted[1]
        get_indexes(start, end, indexes)

    print(indexes)

    duplicates = {k for k, v in Counter(indexes).items() if v > 1}
    print(duplicates)
    print(len(duplicates))

    plt.scatter(marker=",", s=1, *zip(*indexes), alpha=0.2)
    plt.scatter(marker=".", s=1, *zip(*duplicates))

    plt.show()

    # calc(map, indexes)

    # print('\n'.join(['  '.join([f'{cell}' for y, cell in enumerate(row)]) for x, row in enumerate(map)]))

    # cnt = 0

    # for row in map:
    #     for cell in row:
    #         if cell >= 2:
    #             cnt += 1

    # print(cnt)
