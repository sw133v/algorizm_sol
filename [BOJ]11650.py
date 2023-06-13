from collections import defaultdict
def sol_11650():
    res = defaultdict(list)
    for _ in range(int(input())):
        x, y = map(int, input().split())
        res[x].append(y)
        # res[x].sort()
    res = sorted(res.items())
    for xy in res:
        y_list = sorted(xy[1])
        for y in y_list:
            print(f'{xy[0]} {y}')
sol_11650()