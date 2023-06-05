from collections import defaultdict
def sol_1746():
    name = defaultdict(int)
    n, m = map(int, input().split())
    for _ in range(n):
        name[input()] += 1
    for _ in range(m):
        name[input()] += 1
    
    res = sorted([a for a in name if name[a] == 2])
    
    print(len(res))
    for a in res:
        print(a)

sol_1746()