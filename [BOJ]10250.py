def sol_10250():
    def sol_sub():
        h,w,n = map(int, input().split())
        if n == 1:
            print('101')
        else:
            f = n % h +1
            ho = n // h +1
            print('%d%02d'%(f,ho))
    
    for _ in range(int(input())):
        sol_sub()

sol_10250()