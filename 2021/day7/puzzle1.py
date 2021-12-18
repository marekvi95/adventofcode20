import os
from statistics import median

FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")
data = list(map(int, open(FILE).read().split(",")))

print(median(data))

medval = median(data)

sum = 0
for d in data:
    sum += abs(d - medval)

print(sum)
