import sys
def sol_7366():
    res = 0
    n = int(sys.stdin.readline().strip())
    inputList = list(sys.stdin.readline().strip().split())
    
    for word in inputList:
        if word == "sheep":
            res += 1
    
    return res
    
N = int(sys.stdin.readline().strip())
for i in range(N):
    print("Case", str(i+1)+":","This list contains",  (sol_7366()),  "sheep.")
