def sol_10250():
    def sol_sub():
        h,w,n = map(int, input().split())

        fl = n % h
        ho = n // h + 1
        if n % h == 0:
            fl += h
            ho -= 1
        fl *= 100
        print('%03d'%(fl+ho))
    
    for _ in range(int(input())):
        sol_sub()

sol_10250()