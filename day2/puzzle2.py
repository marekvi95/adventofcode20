filename = "C:\\Users\\nxf46245\\Documents\\adventofcode20\\day2\\input.txt"
passwords = list()
letters = list()
ranges = list()

valid_passwords = 0
invalid_passwords = 0

with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]

for line in content:
    splitted = line.split()
    for l in splitted:
        if "-" in l:
            ranges.append(l.split("-")) 
        elif ":" in l:
            letters.append(l.replace(":",""))
        else:
            passwords.append(l)

for x in range(0, len(passwords)):
    # print(passwords[x],ranges[x],letters[x])
    position1 = int(ranges[x][0])
    position2 = int(ranges[x][1])

    if (passwords[x][position1-1] == letters[x]) != (passwords[x][position2-1] == letters[x]):
        print("Password OK", passwords[x], letters[x], position1, position2)
        valid_passwords = valid_passwords + 1
    else:
        print("Password NOK", passwords[x], letters[x], position1, position2)
        invalid_passwords = invalid_passwords + 1
print("Valid passwords: ", valid_passwords)
print("Invalid passwords: ", invalid_passwords)