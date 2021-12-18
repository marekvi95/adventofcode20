import os
import matplotlib.pyplot as plt


def rotate(seq):
    return seq[1:] + seq[:1]


FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")
data = list(map(int, open(FILE).read().split(",")))
# print(data)

fishes = [0] * 9
growth = []

for d in data:
    fishes[d] += 1

print(fishes)
# print(rotate(fishes))

for day in range(256):
    fishes[7] += fishes[0]
    fishes = rotate(fishes)
    growth.append((day, sum(fishes)))
    # print(f'DEN: {day+1} Suma: {sum(fishes)} {fishes}')

print(sum(fishes))
print(growth)

fig = plt.figure()
ax = plt.gca()
ax.scatter(marker=".", s=1, *zip(*growth))
ax.set_yscale("log")
ax.set_xscale("log")
plt.xlabel("Pocet dnu")
plt.ylabel("Pocet ryb")
plt.show()
