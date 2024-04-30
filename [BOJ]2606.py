import sys
from collections import defaultdict
def sol2606():

    n = int(sys.stdin.readline())
    network = defaultdict(list)
    res = set()
    check_point = [1]
    computer_link_list = int(sys.stdin.readline())
    if(computer_link_list == 0):
        print(0)
        return
    
    for _ in range(computer_link_list):
        p, s = map(int, sys.stdin.readline().split())
        network[p].append(s)
        network[s].append(p)
        
    while(len(check_point)):
        temp = check_point.pop(0)
        for a in network[temp]:
            if a in res:
                continue
            check_point.append(a)
            res.add(a)
            
        if temp in res:
            continue
    print(len(res)-1)

sol2606()