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

# print(gamma)
# print(epsilon)

gamma_dec = int(''.join(map(str, gamma)), 2)
epsilon_dec = int(''.join(map(str, epsilon)), 2)

# print(gamma_dec)
# print(epsilon_dec)

print(f"power consumption: {gamma_dec * epsilon_dec}")