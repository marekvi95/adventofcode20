import os
from statistics import mean

FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")
data = list(map(int, open(FILE).read().split(",")))

meanval = round(mean(data)) - 1
print(meanval)

suma = 0
for d in data:
    end = abs(d - meanval)
    suma += sum(range(end + 1))

print(suma)
