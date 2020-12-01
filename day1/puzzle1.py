filename = "C:\\Users\\nxf46245\\Documents\\advent_of_code_2020\\input.txt"
numbers_1 = list()
numbers_2 = list()

with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content] 

print("Task 1")
for x in content:
    c = 2020-int(x)
    if str(c) in content:
        print("Number is: "+str(c))
        numbers_1.append(c)

print("Multiplication of numbers " + str(numbers_1[0]*numbers_1[1])) 

print("Task 2")
for x in content:
    for y in content:
        c = 2020-int(x)-int(y)
        if str(c) in content:
            print("Number is: "+str(c))
            numbers_2.append(c)

numbers_2 = list(set(numbers_2))
print("Multiplication of numbers " + str(numbers_2[0]*numbers_2[1]*numbers_2[2])) 
