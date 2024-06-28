import sys
from collections import defaultdict
def sol_3273():
    N = int(sys.stdin.readline().strip())
    inputData = list(map(int,sys.stdin.readline().strip().split()))
    X = int(sys.stdin.readline().strip())
    res = defaultdict(int)
    inputData = sorted(inputData)
    
    lp = 0 
    hp = N-1
    for i in range(N):
        if res[inputData[i]]:
            continue
        for j in range(hp, -1, -1):
            if inputData[i] >= inputData[j]:
                break
            if inputData[i] + inputData[j] == X:
                res[inputData[i]] = inputData[j]
                hp = j
                break
    result = 0
    for item in res:
        if res[item]:
            result += 1
    print(result)

sol_3273()