import os


def add_val(start, end, map):
    startx = int(start[0])
    starty = int(start[2])
    endx = int(end[0])
    endy = int(end[2])

    if startx == endx:
        nums = range(starty, endy)

        for x, val in enumerate(map):
            for y, val in enumerate(x):
                if y in nums:
                    map[x][y] = "1"


if __name__ == "__main__":
    FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")
    data = open(FILE).read().splitlines()

    print(data)

    X = 10
    Y = 10

    map = [["."] * X for _ in range(Y)]
    print(map)

    for r in data:
        splitted = r.split(" -> ")
        start = splitted[0]
        end = splitted[1]
        add_val(start, end, map)

    print(map)
