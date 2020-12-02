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
    min_range = int(ranges[x][0])
    max_range = int(ranges[x][1])

    count = passwords[x].count(letters[x])
    if count in range(min_range, max_range+1):
        print("Password OK", passwords[x], letters[x], min_range, max_range)
        valid_passwords = valid_passwords + 1
    else:
        print("Password NOK", passwords[x], letters[x], min_range, max_range)
        invalid_passwords = invalid_passwords + 1
print("Valid passwords: ", valid_passwords)
print("Invalid passwords: ", invalid_passwords)