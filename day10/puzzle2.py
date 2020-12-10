import os
from itertools import combinations

filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")


with open(filename) as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]

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

diff = 0
diff_1 = 0
diff_3 = 0
diff_2 = 0
diff_1_list = list()
diff_3_list = list()
diff_2_list = list()


sorted_content = sorted(content)
sorted_content.append(max(sorted_content)+3)
# print(sorted_content)

for x in sorted_content:
    diff = x - diff
    if diff == 1:
        diff_1 += 1
        diff_1_list.append(x)
    elif diff == 3:
        diff_3 += 1
        diff_3_list.append(x)
    else:
        print("not chained")

    diff = x

# print("Diff", diff_1, diff_3)
# print(diff_1*diff_3)
# print(diff_1_list)

chained = 0
to_be_checked = list()

for idx, x in enumerate(diff_1_list):
    new_content = sorted_content.copy()
    to_remove = list_subset(diff_1_list, idx)
    # print(to_remove)
    for number in to_remove:
        new_content = sorted_content.copy()
        # print('new content', new_content)
        for n in number:
            # print("to remove", n)
            new_content.remove(n)
            # print(n)
            # new_content.append(n)
        # print(new_content)
        to_be_checked.append(sorted(new_content))

# print(to_be_checked)
# print(len(to_be_checked))

for x in to_be_checked:
    if is_chained(x):
        chained += 1

print('chained', chained)

# for n in diff_1_list:
#     new_content = sorted_content
#     new_content.remove(n)
#     print(new_content, n)
#     print(is_chained(new_content), new_content)
#     new_content.append(n)
#     new_content.sort()

