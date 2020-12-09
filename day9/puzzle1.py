import os

filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")


with open(filename) as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]

NUMBERS = 25
numbers_list = list()

def is_sum(number, idx):
    # print(content[idx:idx+NUMBERS])
    found = False
    for c in content[idx:idx+NUMBERS]:
        if (number-c) in content[idx:idx+NUMBERS]:
            found = True
    return found



for idx, x in enumerate(content[NUMBERS:]):
    # print(is_sum(x, idx), x)
    if not is_sum(x, idx):
        numbers_list.append(x)

print(numbers_list)