import sys
from collections import deque
def sol_15651():
    def dfs(val):
        nonlocal n, m, check_list
        if val == m:
            print(' '.join(map(str, res)))
            return
        else:
            for i in range(1, n + 1):
                res.append(i)
                dfs(val+1)
                res.pop()
    
    n, m = map(int, sys.stdin.readline().split())
    check_list = [0 for _ in range(n)]
    res = deque()
    
    for i in range(1, n + 1):
        res.append(i)
        dfs(1)
        res.pop()

sol_15651()