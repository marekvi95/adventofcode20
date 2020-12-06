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
        for y in x:
            question.append(y)

questions.append(question)
print(questions)

sum = 0

for x in questions:
    questions_uniq.append(set(x))
    sum += len(set(x))

print(questions_uniq, sum)
