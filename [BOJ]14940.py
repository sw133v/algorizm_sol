import sys
from collections import deque
# sys.setrecursionlimit(1000)

def sol_14940():
    # def dfs(geo, deep):
        
    #     visited[geo[0]][geo[1]] = deep
    #     for i in range(4):
    #         nextX = geo[0] + deltaX[i]
    #         nextY = geo[1] + deltaY[i]
    #         if nextX < 0 or nextX >= N or nextY < 0 or nextY >= M or visited[nextX][nextY] <= deep + 1:
    #             continue
    #         else:
    #             if map_list[nextX][nextY] == 0:
    #                 continue
    #             dfs([nextX, nextY], deep + 1)
            

    deltaX = [0, 1, 0, -1]
    deltaY = [-1, 0, 1, 0]
    map_list = deque([])
    N, M = map(int, sys.stdin.readline().strip().split())
    sys.setrecursionlimit(N*M)
    visited = [[N*M for _ in range(M)]for _ in range(M)]
    # startGeo = []
        for _ in range(M):
        map_list.append(list(map(int, sys.stdin.readline().strip().split())))
    
    # for i in range(M):
    #     if 2 in map_list[i]:
    #         startGeo.append(i)
    #         for j in range(N):
    #             if map_list[i][j] == 2:
    #                 startGeo.append(j)
    #                 break
                
    # dfs(startGeo, 0)
    # for i in range(M):
    #     visited[i] = [0 if x == N*M else x for x in visited[i]]

    # for xLayer in visited:
    #     for yLayer in xLayer:
    #         print(yLayer,end=" ")
    #     print()

sol_14940()