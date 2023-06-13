import sys
from collections import deque
def sol_15650():
    def check(list):
        res = 1
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                res = 0
                break
        return res
    
    def dfs(val):
        nonlocal n, m, check_list
        if val == m:
            if check(res):
                print(' '.join(map(str, res)))
            return
        else:
            for i in range(1, n + 1):
                if check_list[i-1]:
                    continue
                else:
                    check_list[i-1] = 1
                    res.append(i)
                    dfs(val+1)
                    check_list[i-1] = 0
                    res.pop()
    
    n, m = map(int, sys.stdin.readline().split())
    check_list = [0 for _ in range(n)]
    res = deque()
    
    for i in range(1, n + 1):
        check_list[i-1] = 1
        res.append(i)
        dfs(1)
        check_list[i-1] = 0
        res.pop()

sol_15650()