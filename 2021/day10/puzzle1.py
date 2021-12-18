import os
from statistics import median

filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")


with open(filename) as f:
    content = f.readlines()
content = [list(x.strip()) for x in content]

# print(content)

starting = ["(", "[", "{", "<"]
ending = [")", "]", "}", ">"]

conversion = {")": 3, "]": 57, "}": 1197, ">": 25137}
conversion_2 = {"(": 1, "[": 2, "{": 3, "<": 4}
corrupted_sum = 0
incomplete_sum = 0
incomplete_sums = []

for row in content:
    stack = []
    corrupted = False
    for char in row:
        if char in starting:
            stack.append(char)
        else:
            end = stack.pop()
            try:
                if starting.index(end) != ending.index(char):
                    print("Corrupted", char)
                    corrupted = True
                    corrupted_sum += conversion[char]
                    break
            except ValueError:
                print("val error")
                break
    if not corrupted:
        stack.reverse()
        for s in stack:
            val = conversion_2[s]
            incomplete_sum *= 5
            incomplete_sum += val
        print(incomplete_sum)
        incomplete_sums.append(incomplete_sum)
    incomplete_sum = 0


print("Corrupted sum", corrupted_sum)
print("Incomplete sum", median(sorted(incomplete_sums)))
