filename = "C:\\Users\\nxf46245\\Documents\\adventofcode20\\day3\\input.txt"

with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]

y = 0
trees = [0, 0, 0, 0, 0]

for x in content[1:]:
    index = 1+1*y
    if x[index % (len(x))] == '#':
        trees[0] = trees[0] + 1
    # print(x[index % (len(x))])
    # print("index", index % (len(x)))
    y = y+1

y = 0
for x in content[1:]:
    index = 3+3*y
    if x[index % (len(x))] == '#':
        trees[1] = trees[1] + 1
    # print(x[index % (len(x))])
    # print("index", index % (len(x)))
    y = y+1
y = 0
for x in content[1:]:
    index = 5+5*y
    if x[index % (len(x))] == '#':
        trees[2] = trees[2] + 1
    # print(x[index % (len(x))])
    # print("index", index % (len(x)))
    y = y+1
y = 0
for x in content[1:]:
    index = 7+7*y
    if x[index % (len(x))] == '#':
        trees[3] = trees[3] + 1
    # print(x[index % (len(x))])
    # print("index", index % (len(x)))
    y = y+1
y = 0
count = 0
for x in content[1:]:
    count+=1
    if count % 2 == 0: #this is the remainder operator
        index = 1+1*y
        if x[index % (len(x))] == '#':
            trees[4] = trees[4] + 1
        # print(x[index % (len(x))])
        # print("index", index % (len(x)))
        y = y+1

result = 1
for x in trees:
    print("Trees", x)
    result = result * x 
print(result)