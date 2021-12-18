import os
import copy

FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")

file_content = open(FILE).read().splitlines()
content = file_content.copy()
content2 = file_content.copy()

if __name__ == "__main__":
    idx = 0
    while len(content) > 1:
        index_group = [n[idx] for n in content]
        max_index = str(int(index_group.count("1") >= index_group.count("0")))
        content = [n for n in content if n[idx] == max_index]
        idx += 1

    print(content[0])
    idx = 0
    while len(content2) > 1:
        index_group = [n[idx] for n in content2]
        max_index = str(int(index_group.count("1") < index_group.count("0")))
        content2 = [n for n in content2 if n[idx] == max_index]
        idx += 1

    print(content2[0])

    print(int(content[0], 2) * int(content2[0], 2))
