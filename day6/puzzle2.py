import os

filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")
an_sum = 0

for group in open(filename).read().split('\n\n'):
    an_sum += len(set.intersection(*map(set, group.split('\n'))))

print(an_sum)