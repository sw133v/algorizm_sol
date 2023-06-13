import sys

def sol_9663():
    def my_replace(x, y, deep):
        '''
        퀸은 q로
        방문한곳은 깊이로
        방문x는 0으로 하자
        '''
        nonlocal check_point
        
        for i in range(n):
            if check_point[x][i] == 0:
                check_point[x][i] = deep
        
        for i in range(n):
            if check_point[i][y] == 0:
                check_point[i][y] = deep

        for i in range(x, n):
            d = i - x
            left = y - d
            right = y + d
            if left > -1 and check_point[i][left] == 0:
                check_point[i][left] = deep
            if right < n and check_point[i][right] == 0:
                check_point[i][right] = deep

        check_point[x][y] = -1

    def my_breplace(x, y, deep):
        nonlocal n, check_point
        
        for i in range(n):
            if check_point[x][i] == deep or check_point[x][i] == -1:
                check_point[x][i] = 0
        
        for i in range(n):
            if check_point[i][y] == deep or check_point[i][y] == -1:
                check_point[i][y] = 0

        for i in range(x, n):
            d = i - x
            left = y - d
            right = y + d
            if left > -1 and (check_point[i][left] == deep or check_point[i][left] == -1):
                check_point[i][left] = 0
            if right < n and (check_point[i][right] == deep or check_point[i][left] == -1):
                check_point[i][right] = 0

    def backtrack(deep, y):
        nonlocal n
        nonlocal res
        nonlocal check_point
        
        if deep == n:
            res += 1
            return

        else:
            for i in range(n):
                if check_point[deep][i] == 0:
                    my_replace(deep, i, deep + 1)
                    backtrack(deep + 1, i)
                    my_breplace(deep, i, deep + 1)

    n = int(sys.stdin.readline())
    
    check_point = [[0 for _ in range(n)] for _ in range(n)]
    res = 0
    
    for i in range(n):
        my_replace(0, i, 1)
        backtrack(1, i)
        my_breplace(0, i, 1)
    
    print(res)
    
sol_9663()