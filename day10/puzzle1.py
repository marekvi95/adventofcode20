import os

filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")


with open(filename) as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]

diff = 0
diff_1 = 0
diff_2 = 0
diff_3 = 0

sorted_content = sorted(content)
sorted_content.append(max(sorted_content)+3)

for x in sorted_content:
    diff = x - diff
    if diff == 1:
        diff_1 += 1
    elif diff == 2:
        diff_2 += 1
    elif diff == 3:
        diff_3 += 1
    diff = x

print("Diff", diff_1, diff_2, diff_3)
print(diff_1*diff_3)