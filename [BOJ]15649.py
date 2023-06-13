import sys
from collections import deque
def sol_15649():
    # def dfs():
    #     nonlocal res_deque, n, m
    #     # nonlocal n, m
    #     if len(res_deque) == m:
    #         print(' '.join(map(str, res_deque)))
    #         # print(list(res_deque))
    #     else:
    #         for i in range(1, n + 1):
    #             if i in res_deque:
    #                 continue
    #             else:
    #                 res_deque.append(i)
    #                 dfs()
    #                 res_deque.pop()

    # n, m = map(int, sys.stdin.readline().split())
    # res_deque = deque()
    
    # for i in range(1, n + 1):
    #     res_deque.append(i)
    #     dfs()
    #     res_deque.pop()

    def dfs(val):
        nonlocal n, m, check_list
        if val == m:
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

'''
체크포인트 방식이 간소하나 더 빠르다고 판단됨 
230~250ms 체크포인트 방식
270~290ms
'''
sol_15649()