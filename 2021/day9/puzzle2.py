import os

filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")


with open(filename) as f:
    content = f.readlines()
content = [list(x.strip()) for x in content]
content = [[int(x) for x in row] for row in content]

print(content)
sum_min = 0

for i, row in enumerate(content):
    for j, cell in enumerate(row):

        left_move = 1
        while j - left_move >= 0:
            if abs(content[i][j - left_move + 1] - content[i][j - left_move + 1]) == 1:
                left_move += 1
            else:
                break
        try:
            right = content[i][j + 1]
        except IndexError:
            right = 9
        try:
            bottom = content[i + 1][j]
        except IndexError:
            bottom = 9
        if i - 1 >= 0:
            top = content[i - 1][j]
        else:
            top = 9
        minimum = []
        minimum.append(left)
        minimum.append(top)
        minimum.append(right)
        minimum.append(bottom)

        # minimum.append(cell)

        if min(minimum) > cell:
            sum_min += cell + 1

print(sum_min)
