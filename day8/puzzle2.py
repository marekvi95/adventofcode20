import os

filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")

with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]




instructions = list()
jumps_index = list()
nops_index = list()

for i, x in enumerate(content):
    instruction = x.split(' ')[0]
    operation = int(x.split(' ')[1])
    instructions.append({instruction: operation})
    if instruction == 'jmp':
        jumps_index.append(i)
    elif instruction == 'nop':
        nops_index.append(i)


# print(instructions)

print('CHANGING JUMPS')
for x in jumps_index:
    instructions[x]['nop'] = instructions[x]['jmp']
    del instructions[x]['jmp']
    # old_val = instructions[x]['jmp']
    # instructions[x]['jmp'] = 0
    # print(instructions)
    program_counter = 0
    accumulator = 0
    visited = list()
    visited.append(0)
    loop_detected = False

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
                # print('Loop detected', list(instructions[program_counter].keys())[0], list(instructions[program_counter].values())[0], program_counter, accumulator)
                loop_detected = True
                # program_counter += 1
                break
        # print(list(instructions[program_counter].keys())[0], list(instructions[program_counter].values())[0], program_counter, accumulator)
    if loop_detected == False:
        print(accumulator)
    # print(visited)
    # print(nops_index, jumps_index)
    # instructions[x]['jmp'] = old_val
    instructions[x]['jmp'] = instructions[x]['nop']
    del instructions[x]['nop']

print("NOPS CHANGING")
for x in nops_index:
    instructions[x]['jmp'] = instructions[x]['nop']
    del instructions[x]['nop']
    # old_val = instructions[x]['jmp']
    # instructions[x]['jmp'] = 0
    # print(instructions)
    program_counter = 0
    accumulator = 0
    visited = list()
    visited.append(0)
    loop_detected = False

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
                # print('Loop detected', list(instructions[program_counter].keys())[0], list(instructions[program_counter].values())[0], program_counter, accumulator)
                loop_detected = True
                # program_counter += 1
                break
        # print(list(instructions[program_counter].keys())[0], list(instructions[program_counter].values())[0], program_counter, accumulator)
    if loop_detected == False:
        print(accumulator)
    # print(visited)
    # print(nops_index, jumps_index)
    # instructions[x]['jmp'] = old_val
    instructions[x]['nop'] = instructions[x]['jmp']
    del instructions[x]['jmp']