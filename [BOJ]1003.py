from collections import defaultdict
def sol_1003():
    def fivo(n):
        nonlocal dp

        if dp[n]:
            return dp[n]
        
        else:
            a, b = fivo(n-1), fivo(n-2)
            dp[n] = [x + y for x,y in zip(a, b)] 
            return dp[n]

    dp = defaultdict(list)
    dp[0].append(1)
    dp[0].append(0)
    dp[1].append(0)
    dp[1].append(1)
    
    for _ in range(int(input())):
        for a in fivo(int(input())):
            print(a,end=' ')
        print()

sol_1003()