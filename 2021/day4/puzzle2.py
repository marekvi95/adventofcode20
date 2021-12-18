import os


def bingo(m, bingo_list):
    for idx, mm in enumerate(m):
        if idx in bingo_list:
            continue
        for row in mm:
            count = sum(map(lambda x: "w" in x, row))
            if count > 4:
                return True

        for column in zip(*mm):
            count = sum(map(lambda x: "w" in x, column))
            if count > 4:
                return True

    return False


def calc_result(m, last_number):
    sum = 0
    for row in m:
        for c in row:
            if "w" not in c:
                sum += int(c)

    print(f"Sum {sum} last number {last_number} result {sum*int(last_number)}")


if __name__ == "__main__":
    FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")
    data = open(FILE).read()

    data_lst = data.split("\n\n")
    vals = data_lst[0]

    m = []

    for board in data_lst[1:]:
        m.append(
            [
                [num.strip() for num in line.strip().split(" ") if num.strip() != ""]
                for line in board.split("\n")
            ]
        )

    print(vals)
    cnt = 0
    bingo_cnt = 0
    bingo_list = []

    for v in vals.split(","):
        cnt += 1
        for x in range(len(m)):
            for col in range(5):

                for row in range(5):
                    # print(m[x][row][col])
                    if v == m[x][row][col]:
                        m[x][row][col] += "w"
                    if cnt >= 5:
                        if x not in bingo_list:
                            if bingo(m, bingo_list):
                                print("BINGO")
                                print(m[x])
                                print(x)
                                bingo_list.append(x)
                                if len(bingo_list) == len(m):
                                    calc_result(m[x], v)
                                    exit()
