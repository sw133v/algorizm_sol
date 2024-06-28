import sys
def sol_3699():
    h, l = map(int, sys.stdin.readline().strip().split())
    parkingStation = []
    res = 0
    isOdd = 0
    if l % 2:
        isOdd = 1
        
    for _ in range(h):
        parkingStation.append(list(map(int,sys.stdin.readline().strip().split())))
        
    for car in range(h * l):
        for floor in range(h):
            if car in parkingStation[floor]:
                carIndex = parkingStation[floor].index(car)
                if carIndex < l // 2 + isOdd:
                    res += 5 * carIndex
                else:
                    res += 5 * (l - carIndex) 
                res += floor * 20
                parkingStation[floor] = parkingStation[floor][carIndex:] + parkingStation[floor][:carIndex]
                break
    print(res)

N = int(sys.stdin.readline().strip())
for _ in range(N):
    sol_3699()