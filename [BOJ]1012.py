import sys
from collections import deque
def sol_1012():
    def mainSolAl():
        def delta(n):
            x = [0, 1, 0, -1]
            y = [-1, 0, 1, 0]

        res = 0
        rowDict = defaultdict(list)
        # visit = defaultdict(list)

        row, col, cabages = map(int, sys.stdin.readline().split())
        for _ in range(cabages):
            cabageRow, cabageCol = map(int, sys.stdin.readline().split())
            rowDict[cabageRow].append(cabageCol)

        # print(rowDict)
        for i in rowDict:
            print(i, rowDict[i])

        # while rowDict:
        #     tempPoint = -1
        #     for i in rowDict:
        #         if rowDict[i]:
        #             tempPoint = i
        #             break;

            

        #     res += 1


        # print(res)

    # case = map(int, sys.stdin.readline())
    case = int(sys.stdin.readline())

    for _ in range(case):
        mainSolAl()
    # print(case)

sol_1012()