import sys
from collections import deque
def sol_15657():
    def dfs(val):
        if val == m:
            if promise(res):
                return
            print(' '.join(map(str, res)))
            return
        else:
            for i in range(n):
                res.append(datas[i])
                dfs(val+1)
                res.pop()

    def promise(li):
        res = 0
        for i in range(len(li)-1):
            if li[i] > li[i+1]:
                res = 1
                break
        return res
    
    n, m = map(int, sys.stdin.readline().split())
    datas = sorted(list(map(int, sys.stdin.readline().split())))
    res = deque()
    
    for i in range(n):
        res.append(datas[i])
        dfs(1)
        res.pop()

sol_15657()