import os
from itertools import combinations
import time

def list_subset(arr, r):
    return list(combinations(arr, r))

def is_chained(arr):
    diff = 0
    for idx, x in enumerate(arr):
        diff = x - diff
        # print(diff, x)
        if diff not in [1,2,3]:
            return False
        diff = x
        if idx == len(arr)-1:
            return True

def uniq(lst):
    last = object()
    for item in lst:
        if item == last:
            continue
        yield item
        last = item

def sort_and_deduplicate(l):
    return list(uniq(sorted(l, reverse=True)))

if __name__ == "__main__":
    filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")
    with open(filename) as f:
        content = f.readlines()
    content = [int(x.strip()) for x in content]

    diff = 0
    diff_1_list = list()

    start_time = time.time()

    sorted_content = sorted(content)
    sorted_content.append(max(sorted_content)+3)

    for x in sorted_content:
        diff = x - diff
        if diff == 1:
            diff_1_list.append(x)
        diff = x

    chained = 0
    to_be_checked = list()

    for idx, x in enumerate(diff_1_list):
        new_content = sorted_content.copy()
        to_remove = list_subset(diff_1_list, idx)
        for number in to_remove:
            new_content = sorted_content.copy()
            for n in number:
                new_content.remove(n)
            to_be_checked.append(sorted(new_content))
        if idx > len(diff_1_list)//2:
            break

    # print(to_be_checked)
    # print(len(to_be_checked))


    # for l in to_be_checked:
    #     # print(len(l))
    #     if len(l) < 9 or l[0] > 3:
    #         to_be_checked.remove(l)

    # print(len(to_be_checked))

    for x in to_be_checked:
        if is_chained(x):
            chained += 1

    print('chained', chained)
    print("--- %s seconds ---" % (time.time() - start_time))
