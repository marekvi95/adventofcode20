from string import ascii_lowercase

filename = "C:\\Users\\nxf46245\\Documents\\adventofcode20\\day6\\input.txt"

with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]

questions = list()
question = list()
questions_uniq = list()

for x in content:
    if len(x) == 0:
        questions.append(question)
        question = list()
    else:
        question.append(x)

questions.append(question)
print(questions)

sum = 0
cnt = 0


for x in questions:
    for c in ascii_lowercase:    
        # print(range(len(x)), x, c)
        for i in range(len(x)):
            if c in x[i]:
                cnt += 1
                if cnt == len(x):
                    # print("tada", cnt, x[i], c)
                    sum += 1
                    cnt = 0
            else:
                cnt = 0


print(sum)

