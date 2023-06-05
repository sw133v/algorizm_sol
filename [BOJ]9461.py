def sol9461():
    def recur(n):
        nonlocal dp
        if dp[n]: 
            return dp[n]
        else:
            dp[n] = recur(n-2) + recur(n-3)  
            return dp[n]

    dp = [1, 1, 1]
    dp += [0 for _ in range(97)]

    for _ in range(int(input())):
        print(recur(int(input())-1))

sol9461()