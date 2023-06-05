from collections import defaultdict
def sol1721():
    sites = defaultdict(str)
    n, m = map(int, input().split())
    for _ in range(n):
        site, password = input().split()
        sites[site] = password
    
    for _ in range(m):
        print(sites[input()])

sol1721()