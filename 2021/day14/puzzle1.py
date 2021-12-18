import os

filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")


data = open(filename).read().splitlines()

print(data)

start = data[0]
new = start

print(start)
rules = data[2:]
to_be_inserted = []

for step in range(1, 5):
    start = new
    for rule in rules:
        r = rule.split(" -> ")
        idx = start.find(r[0])
        if idx >= 0:
            new = new[: idx + 1] + r[1] + new[idx + 1 :]

    print(step, new, len(new))
