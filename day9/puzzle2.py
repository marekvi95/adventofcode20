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

found = False

for idx, x in enumerate(content):
    suma = 0
    idx2 = idx
    for y in content[idx:]:
        suma += y
        # print(suma)
        idx2 += 1
        if suma > numbers_list[0]:
            break
        if suma == numbers_list[0]:
            print('found', content[idx:idx2])
            cont_range = content[idx:idx2]
            found = True
            break
    if found:
        break

print("Sum of max and min", max(cont_range) + min(cont_range))