import os

filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")

with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]


records = dict()
record_dict = dict()


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

for x in content:
    record = x.replace('bags', '').replace('bag', '').replace('.','').replace('no other','').strip().split(' contain')
    key = record[0].strip()
    record[1] = ''.join([i for i in record[1] if not i.isdigit()]).strip()
    vals = record[1].split(' ,  ')  
    record_dict[key] = vals
    records.update(record_dict)

# print(records)
# print("Vsechny barvy", len(records))


suma = 0
paths_list = list()

for key in records:
    try:
        paths = find_all_paths(records, key, 'shiny gold')
        suma += len(paths)
        paths_list.extend(paths)
        # print("Cesta pro ", key, paths)
    except KeyError:
        # print("Cesta nenalezena ", key)
        pass

# print(suma)
# print(len(paths_list))
# print(paths_list)
colors = list()
for x in paths_list:
    colors.extend(x)
print(set(colors))
print("Set barev", len(set(colors))-1)
