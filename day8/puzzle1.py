import os

filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")

with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]

program_counter = 0
accumulator = 0

instructions = list()
visited = list()

for x in content:
    instruction = x.split(' ')[0]
    operation = int(x.split(' ')[1])
    instructions.append({instruction: operation})

print(instructions)

visited.append(0)

while program_counter < len(instructions):
    if list(instructions[program_counter].keys())[0] == 'nop':
        program_counter += 1
        visited.append(program_counter)
    elif list(instructions[program_counter].keys())[0] == 'acc':
        accumulator += list(instructions[program_counter].values())[0]
        program_counter += 1
        visited.append(program_counter)
    elif list(instructions[program_counter].keys())[0] == 'jmp':
        if (program_counter + list(instructions[program_counter].values())[0]) not in visited:
            program_counter += list(instructions[program_counter].values())[0]
            visited.append(program_counter)
        else:
            print('Loop detected', accumulator)
            break
    print(program_counter, accumulator)

print(visited)