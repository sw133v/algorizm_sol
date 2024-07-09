import sys
from collections import defaultdict
from copy import deepcopy
def sol_1012():
    def mainSolAl():
        def delta(coordinate):
            deltaX = [0, 1, 0, -1]
            deltaY = [-1, 0, 1, 0]
            
            for i in range(4):
                if (coordinate[0] + deltaX[i]) < 0 or (coordinate[0] + deltaX[i] >= row ):
                    continue
                if (coordinate[1] + deltaY[i]) < 0 or (coordinate[1] + deltaY[i] >= col ):
                    continue
                
                if visit[coordinate[0] + deltaX[i]][coordinate[1] + deltaY[i]] and (coordinate[1] + deltaY[i]) in tempDict[coordinate[0] + deltaX[i]]:
                    visit[coordinate[0] + deltaX[i]][coordinate[1] + deltaY[i]] = 0
                    delta([coordinate[0] + deltaX[i], coordinate[1] + deltaY[i]])

        res = 0
        rowDict = defaultdict(list)
        row, col, cabages = map(int, sys.stdin.readline().split())
        visit = [[1 for _ in range(col)] for _ in range(row)]
        
        for _ in range(cabages):
            cabageRow, cabageCol = map(int, sys.stdin.readline().split())
            rowDict[cabageRow].append(cabageCol)
            
        tempDict = deepcopy(rowDict)

        for i in rowDict:
            for j in rowDict[i]:
                if (visit[i][j]):
                    res += 1
                    visit[i][j] = 0
                    delta([i, j])
        print(res)

    case = int(sys.stdin.readline())

    for _ in range(case):
        mainSolAl()

sol_1012()