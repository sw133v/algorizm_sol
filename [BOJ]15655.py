import sys
from collections import deque
def sol_15655():
    def dfs(val):
        nonlocal n, m, check_list
        if val == m:
            if promise(res):
                print(' '.join(map(str, res)))
            return
        else:
            for i in range(n):
                if check_list[i]:
                    continue
                else:
                    check_list[i] = 1
                    res.append(datas[i])
                    dfs(val+1)
                    check_list[i] = 0
                    res.pop()

    def promise(li):
        temp = sorted(li)
        if list(li) == temp:
            return 1
        return 0
    
    n, m = map(int, sys.stdin.readline().split())
    check_list = [0 for _ in range(n)]
    datas = sorted(list(map(int, sys.stdin.readline().split())))
    res = deque()
    
    for i in range(n):
        check_list[i] = 1
        res.append(datas[i])
        dfs(1)
        check_list[i] = 0
        res.pop()

sol_15655()