import os

FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")

with open(FILE) as f:
    content = f.read().splitlines()

# 0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6
digit_lengths = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
count = 0

two_digits = []
three_digits = []
four_digits = []
five_digits = []
six_digits = []
seven_digits = []

suma = 0

for c in content:
    line = c.split("|")[0].strip().split(" ")
    # print(line)

    two_digits = []
    three_digits = []
    four_digits = []
    five_digits = []
    six_digits = []
    seven_digits = []

    for s in line:
        if len(s) == 2:
            two_digits.append(s)
        elif len(s) == 3:
            three_digits.append(s)
        elif len(s) == 4:
            four_digits.append(s)
        elif len(s) == 5:
            five_digits.append(s)
        elif len(s) == 6:
            six_digits.append(s)
        elif len(s) == 7:
            seven_digits.append(s)

    one = two_digits[0]
    seven = three_digits[0]
    four = four_digits[0]
    eight = seven_digits[0]

    zero = 0
    two = 0
    three = 0
    five = 0
    six = 0
    nine = 0

    right = two_digits[0]
    top = " ".join(set(three_digits[0]).difference(right))
    middle_top_left = " ".join(set(four_digits[0]).difference(right))

    for n in six_digits:
        if four[0] in n and four[1] in n and four[2] in n and four[3] in n:
            nine = n
        elif right[0] in n and right[1] in n:
            zero = n
        else:
            six = n

    top_right = " ".join(set(zero).difference(six))

    for n in five_digits:
        if top in n and right[0] in n and right[1] in n:
            three = n
        elif top_right in n:
            two = n
        else:
            five = n

    numbers = [zero, one, two, three, four, five, six, seven, eight, nine]
    output = c.split("|")[1].strip().split(" ")
    result = []

    for o in output:
        for idx, word in enumerate(numbers):
            word_list = list(word)
            o_list = list(o)
            if sorted(word_list) == sorted(o_list):
                # print(idx)
                result.append(idx)

    result_str = [str(integer) for integer in result]
    suma += int("".join(result_str))

    # print(f" TOP: {top}, RIGHT: {right}")
    # print(f"ZERO {zero}, ONE: {one}, TWO {two}, THREE {three}, FOUR: {four}, FIVE: {five} SIX {six}, SEVEN: {seven}, EIGHT {eight}, NINE {nine}")
print(suma)
