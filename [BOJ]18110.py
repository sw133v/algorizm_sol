import sys
from collections import defaultdict

def sol18110():
    def trimmed(value):
        res = value * 15 / 100
        return ban(res)
    
    def ban(value):
        res = value // 1
        if (value - res) // 0.5:
            res += 1
        return int(res)
    
    n = int(sys.stdin.readline())
    if n == 0:
        print(0)
        return
    
    defi = defaultdict(int)
    li = []

    for _ in range(n):
        defi[int(sys.stdin.readline())] += 1

    for i in range(31):
        for _ in range(defi[i]):
            li.append(i)

    trimmed_mean = trimmed(n)
    print(ban(sum(li[trimmed_mean: None if trimmed_mean == 0 else -trimmed_mean]) / (n - 2 * trimmed_mean)))
    
sol18110()