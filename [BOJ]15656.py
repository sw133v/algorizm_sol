import sys
from collections import deque
def sol_15656():
    def dfs(val):
        if val == m:
            print(' '.join(map(str, res)))
            return
        else:
            for i in range(n):
                res.append(datas[i])
                dfs(val+1)
                res.pop()

    def promise(li):
        temp = sorted(li)
        if list(li) == temp:
            return 1
        return 0
    
    n, m = map(int, sys.stdin.readline().split())
    datas = sorted(list(map(int, sys.stdin.readline().split())))
    res = deque()
    
    for i in range(n):
        res.append(datas[i])
        dfs(1)
        res.pop()

sol_15656()