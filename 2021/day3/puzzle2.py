import os
import copy

FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")


def calculate(gamma, epsilon, content):
    ones = 0
    zeros = 0

    for d in range(0, len(content[0])):
        for n in range(0, len(content)):
            if int(content[n][d]) == 1:
                ones = ones + 1
            elif int(content[n][d]) == 0:
                zeros = zeros + 1

        if ones >= zeros:
            gamma[d] = 1
            epsilon[d] = 0
        else:
            gamma[d] = 0
            epsilon[d] = 1

        zeros = 0
        ones = 0

    # print(gamma)


if __name__ == "__main__":
    with open(FILE) as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    # gamma = [0] * len(content[0])
    # epsilon = [0] * len(content[0])
    # blank = '9' * len(content[0])

    # # print(content)
    # calculate(gamma, epsilon, content)
    # # print(gamma)

    # content2 = copy.deepcopy(content)

    # def stop_iter(lst):
    #     return True if lst.count(blank) == (len(lst)-1) else False

    # for d in range(0, len(content[0])):
    #     for n in range(0, len(content)):
    #         calculate(gamma, epsilon, content)
    #         if int(content[n][d]) != gamma[d]:
    #             content[n] = blank
    #         if stop_iter(content):
    #             break

    # for d in range(0, len(content2[0])):
    #     for n in range(0, len(content2)):
    #         calculate(gamma, epsilon, content2)
    #         if int(content2[n][d]) != epsilon[d]:
    #             content2[n] = blank
    #         if stop_iter(content2):
    #             break

    # # print(content)
    # # print(content2)

    # oxygen = [s for s in content if s != blank]
    # carbon = [s for s in content2 if s != blank]

    # # print(int(oxygen[0],2))
    # # print(int(carbon[0],2))
    # print(f"result: {int(oxygen[0], 2)*int(carbon[0],2)}")

    input_file = open(FILE).read().splitlines()

    def part_one():
        y = [[z[i] for z in input_file] for i in range(len(input_file[0]))]
        gamma = [max(x, key=x.count) for x in y]
        epsilon = [min(x, key=x.count) for x in y]

        return int("".join(gamma), 2) * int("".join(epsilon), 2)

    def part_two():
        ogr = input_file.copy()
        idx = 0
        while len(ogr) > 1:
            grouped_by_idx = [num[idx] for num in ogr]
            max_index = str(int(grouped_by_idx.count("1") >= grouped_by_idx.count("0")))
            ogr = [num for num in ogr if num[idx] == str(max_index)]
            idx += 1
        ogr = ogr[0]

        co2 = input_file.copy()
        idx = 0
        while len(co2) > 1:
            grouped_by_idx = [num[idx] for num in co2]
            min_index = str(int(grouped_by_idx.count("1") < grouped_by_idx.count("0")))
            co2 = [num for num in co2 if num[idx] == min_index]
            idx += 1

        co2 = co2[0]
        return int("".join(ogr), 2) * int("".join(co2), 2)

    print(f"part_one: {part_one()}")
    print(f"part_two: {part_two()}")
