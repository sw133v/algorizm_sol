import sys
def sol_17350():
    n = int(sys.stdin.readline().strip())
    listData = []
    for _ in range(n):
        listData.append(sys.stdin.readline().strip())
    
    if "anj" in listData:
        print("뭐야;")
    else:
        print("뭐야?")

sol_17350()