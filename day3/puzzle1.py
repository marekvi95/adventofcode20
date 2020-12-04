filename = "C:\\Users\\nxf46245\\Documents\\adventofcode20\\day3\\input.txt"

with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]

y = 0
trees = 0

for x in content[1:]:
    # print(x)
    # print(len(x))
    index = 3+3*y
    if x[index % (len(x))] == '#':
        trees = trees + 1
    print(x[index % (len(x))])
    print("index", index % (len(x)))
    # print("y",y)
    y = y+1
    
print("Trees", trees)