import sys
def sol_30802():
    N, T, P = None, None, None
    Size = []
    
    N = int(sys.stdin.readline())
    Size = list(map(int, sys.stdin.readline().strip().split()))
    T, P = map(int, sys.stdin.readline().strip().split())
    resT = 0
    for size in Size:
        if(size % T):
            resT += 1
        resT += (size // T)
        # print("묶음",size // T)
        # print("나머지",size % T)
    
    print(resT)
    print(N // P, N % P)
    
sol_30802()