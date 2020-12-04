filename = "C:\\Users\\nxf46245\\Documents\\adventofcode20\\day4\\input.txt"

with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]

passports = list()
passport = ""

expected = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']

for x in content:
    passport += ' '
    if len(x) == 0:
        passports.append(passport)
        passport = ""
    else:
        passport += x

passports.append(passport)

print(passports)

cnt = 0
right = 0

for x in passports:
    for val in expected:
        if val in x:
            cnt += 1
    if cnt == len(expected):
        right += 1
    cnt = 0

print(right)

