def sol_2738():
    n, m = map(int, input().split())
    a = []
    b = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    
    for _ in range(n):
        b.append(list(map(int, input().split())))
    
    res = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(a[i][j]+b[i][j])
        res.append(temp)

    for i in range(n):
        for j in res[i]:
            print(j, end=' ')
        print()
    
sol_2738()