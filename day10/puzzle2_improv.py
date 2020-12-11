import os
import more_itertools as mit
import time

if __name__ == "__main__":
    filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")
    with open(filename) as f:
        content = f.readlines()
    content = [int(x.strip()) for x in content]
    start_time = time.time()
    content.append(max(content)+3)
    content.append(0)
    sorted_content = sorted(content)
    groups = [list(group) for group in mit.consecutive_groups(sorted_content)]
    suma = 1
    
    for g in groups:
        if len(g) > 2:
            if len(g) == 5:
                suma = suma * 7
            elif len(g) == 4:
                suma = suma * 4
            elif len(g) == 3:
                suma = suma * 2
            
    print(suma)
    print("--- %s seconds ---" % (time.time() - start_time))
