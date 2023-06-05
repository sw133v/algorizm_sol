import sys
from collections import defaultdict
def sol2606():
    def woram(val):
        nonlocal computers
        for i in network[val]:
            if computers[i]:
                continue
            computers[i] = 1
            woram(i)

    n = int(sys.stdin.readline())
    computers = [0 for i in range(n+1)]
    network = defaultdict(list)
    for _ in range(int(sys.stdin.readline())):
        p, s = map(int, sys.stdin.readline().split())
        network[p].append(s)
        network[s].append(p)
    woram(1)
    print(computers.count(1)-1)

sol2606()