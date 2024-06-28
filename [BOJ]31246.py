import sys
from collections import defaultdict
def sol_31246():
    #광고 갯수 N, 목표 수 K
    N, K = map(int, sys.stdin.readline().strip().split())
    AD_list = []
    get_AD = 0
    cost = 0
    cost_raise = defaultdict(int)
    for _ in range(N):
        # 입찰가 A, 실제가격 B
        A, B = map(int, sys.stdin.readline().strip().split())
        if A >= B:
            get_AD += 1
        else:
            AD_list.append([A, B])
            cost_raise[B-A] += 1
                
    if get_AD >= K:
        print(0)
    else:
        cost_raise = sorted(cost_raise.items())
        # cost_raise = sorted(cost_raise)
        for i in cost_raise:
            # print(i)
            cost = i[0]
            get_AD += i[1]
            if get_AD >= K:
                break
        print(cost)

sol_31246()