filename = "C:\\Users\\nxf46245\\Documents\\adventofcode20\\day5\\input.txt"

with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]

ids = list()

for x in content:
    board = range(0,128)
    col = range(0,8)
    for ch in x[:-3]:
        boardlen = len(board)
        midx = boardlen//2
        first_half = board[:midx]
        second_half = board[midx:]
        if ch == 'B':
            board = second_half
        elif ch == 'F':
            board = first_half
    for ch in x[-3:]:
        collen = len(col)
        midx = collen//2
        first_half = col[:midx]
        second_half = col[midx:]
        if ch == 'R':
            col = second_half
        elif ch == 'L':
            col = first_half

    id = board[0] * 8 + col[0]
    if board[0] != 0 or board[0] != 127:
        ids.append(id)
    # print(board[0], col[0], id)

maxid = max(ids)
print(maxid)
count = 0
for i in range(1, maxid):
    if i in ids:
        count += 1
    else:
            # count = 0
        print('Missing id', i)
        # if count > 3:
            # print('ID found', i)

if 652 in ids and 654 in ids:
    print("ok")