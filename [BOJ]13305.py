import sys
def sol_13305():
    cities = int(sys.stdin.readline().strip())
    dist = list(map(int, sys.stdin.readline().strip().split()))
    oil_cost = list(map(int, sys.stdin.readline().strip().split()))
    
    res = oil_cost[0] * dist[0]
    
    best_cost = oil_cost[0]
    
    for i in range(1, cities - 1):
        if oil_cost[i] < best_cost:
            best_cost = oil_cost[i]
        res += best_cost * dist[i]
    print(res)

sol_13305()