import sys
from collections import defaultdict
def sol_8979():
    N, K = map(int, sys.stdin.readline().strip().split())
    all_rank = defaultdict(list)
    rank = 1
    
    for _ in range(N):
        CON, G, S, B = map(int, sys.stdin.readline().strip().split())
        all_rank[(G, S, B)].append(CON)
    
    temp_rank = sorted(all_rank.keys())
    temp_rank.reverse()
    for i in temp_rank:
        if K in all_rank[i]:
            break
        rank += len(all_rank[i])
    print(rank)

sol_8979()