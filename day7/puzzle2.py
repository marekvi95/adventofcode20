import os

filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")

with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]


records = dict()
record_dict = dict()
global_count = 0


def traverse_graph(graph, start, src_count):
    for child in graph[start]:
        child_key = list(child.keys())[0]
        count = int(list(child.values())[0])
        count_to_add = count * src_count
        # print(count_to_add)
        global global_count
        global_count += count_to_add
        # print(child_key, count)
        traverse_graph(graph, child_key, count_to_add)


for x in content:
    record = x.replace('bags', '').replace('bag', '').replace('.','').replace('no other','').strip().split(' contain')
    key = record[0].strip()
    vals = record[1].split(', ')
    record_dict[key] = list()
    for v in vals:
        if len(v) > 0:
            color = ' '.join(v.strip().split(' ')[1:])  
            number = v.strip().split(' ')[0]
            # print(key, color, number)
            my_dict = {}
            my_dict[color] = number
            record_dict[key].append(my_dict)
    records.update(record_dict)


traverse_graph(records, 'shiny gold', 1)
print(global_count)