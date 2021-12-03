import os

filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")


with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]

# print(content)
ones = 0
zeros = 0
gamma = []
epsilon = []

for d in range(0, len(content[0])):
    for n in range(0, len(content)-1):
        if int(content[n][d]) == 1:
            ones = ones + 1
        else:
            zeros = zeros + 1
    gamma.append(1) if ones > zeros else gamma.append(0)
    epsilon.append(0) if ones > zeros else epsilon.append(1)
    zeros = 0
    ones = 0

print(content)
print(gamma)

for d in range(0, len(content[0])):
    for n in range(0, len(content)-1):
        if int(content[n][d]) == 1:
            ones = ones + 1
        else:
            zeros = zeros + 1
    gamma.append(1) if ones > zeros else gamma.append(0)
    epsilon.append(0) if ones > zeros else epsilon.append(1)
    zeros = 0
    ones = 0