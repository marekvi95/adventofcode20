filename = "C:\\Users\\nxf46245\\Documents\\adventofcode20\\day4\\input.txt"

def check_string(string):
    key = string.partition(delim)[0]
    val = string.partition(delim)[2]
    print(key, val)

    if 'byr' in key:
        if int(val) in range(1920,2003):
            return True
        else:
            return False
    elif 'iyr' in key:
        if int(val) in range(2010, 2021):
            return True
        else:
            return False
    elif 'eyr' in key:
        if int(val) in range(2020, 2031):
            return True
        else:
            return False
    elif 'hgt' in key:
        if 'cm' in val:
            print(int(val[:-2]) )
            if int(val[:-2]) in range(150, 194):
                return True
            else:
                return False
        elif 'in' in val:
            if int(val[:-2]) in range(59, 77):
                return True
            else:
                return False
        else:
            return False
    elif 'hcl' in key:
        if '#' in val[0]:
            if len(val) == 7 and val[1:].isalnum():
                return True
            else:
                return False
        else:
            return False
    elif 'ecl' in key:
        if val == 'amb':
            return True
        elif val == 'blu':
            return True
        elif val == 'brn':
            return True
        elif val == 'gry':
            return True
        elif val == 'grn':
            return True
        elif val == 'hzl':
            return True
        elif val == 'oth':
            return True
        else: 
            return False
    elif 'pid' in key:
        if val.isnumeric() and len(val) == 9:
            return True
        else:
            return False
    else:
        return False



with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]

passports = list()
passports_checked = list()
passport = ""

expected = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
delim = ':'

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
            found = x.rfind(val)
            print(x[found:found+len(val)])
    if cnt == len(expected):
        right += 1
        passports_checked.append(x)
    cnt = 0

print(right)
print(passports_checked)

right_passports = 0

for x in passports_checked:
    vals = x.split()
    print('Password --- :')
    checked = 0
    for v in vals:
        # print(v)
        if check_string(v):
            checked += 1
        print(v, check_string(v))
    print(checked)
    if checked == 7:
        right_passports += 1

print('Right passports: ', right_passports)
        

