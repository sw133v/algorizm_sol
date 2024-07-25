import sys
from collections import deque
from pprint import pprint
from copy import deepcopy

def sol_14940():
    deltaX = [0, 1, 0, -1]
    deltaY = [-1, 0, 1, 0]
    map_list = deque()
    N, M = map(int, sys.stdin.readline().strip().split())
    visited = [[False for _ in range(M)]for _ in range(N)]
    res = [[0 for _ in range(M)]for _ in range(N)]
    start_x = None
    start_y = None
    task_queue = deque()
    length = 0
    
    for _ in range(N):
        map_list.append(list(map(int, sys.stdin.readline().strip().split())))
    
    for i in range(N):
        for j in range(M):
            if map_list[i][j] == 2:
                start_x = i
                start_y = j
            if map_list[i][j] == 0:
                visited[i][j] = True
                
    task_queue.append([[start_x, start_y], ])
    
    while task_queue:
        temp_que = deque()
        task = task_queue.popleft()
        for index in task:
            res[index[0]][index[1]] = length
            visited[index[0]][index[1]] = True
            
            for i in range(4):
                next_x = index[0] + deltaX[i]
                next_y = index[1] + deltaY[i]
                if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M:
                    continue
                if visited[next_x][next_y]:
                    continue
                if [next_x, next_y] in temp_que:
                    continue
                temp_que.append([next_x, next_y])
        if temp_que != deque():
            task_queue.append(temp_que)
        length += 1

    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                continue
            if map_list[i][j]:
                res[i][j] = -1

    for xLayer in res:
        print(' '.join(map(str, xLayer)))    

sol_14940()