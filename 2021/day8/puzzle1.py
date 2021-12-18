import os
from statistics import median

FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")

with open(FILE) as f:
    content = f.read().splitlines()

digits = [2, 4, 3, 7]
count = 0

for c in content:
    line = c.split("|")[1].strip().split(" ")
    # print(line)
    # sum((len(s) for s in line) if len(s) in digits)
    for s in line:
        if len(s) in digits:
            count += 1

print(count)
