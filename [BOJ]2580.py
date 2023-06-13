import sys
# import time

def sol_2580():
    def promise(x, y, n):
        # 행
        res = 1
        temp = plate[x]
        if n in temp:
            return 0
        # 열
        for i in range(9):
            if plate[i][y] == n:
                res = 0
                break
        # 네모칸
        for i in range(x // 3 * 3, x // 3 * 3 + 3):
            if res:
                for j in range(y // 3 * 3, y // 3 * 3 + 3):
                    if plate[i][j] == n:
                        res = 0
                        break
            else:
                break
        return res

    def sdoku(x):
        nonlocal plate, is_end
        if is_end:
            if fine(x):
                for i in range(9):
                    print(' '.join(map(str, plate[i])))
                is_end = False
                return

            else:
                for i in range(x, 9):
                    for j in range(9):
                        if plate[i][j]:
                            continue
                        for n in range(1, 10):
                            if promise(i, j, n):
                                plate[i][j] = n
                                sdoku(i)
                                plate[i][j] = 0
            return
        return

    def fine(x):
        nonlocal plate
        res = 1
        for i in range(x, 9):
            if 0 in plate[i]:
                res = 0
                break
        return res

    plate = []
    is_end = True
    for _ in range(9):
        plate.append(list(map(int, sys.stdin.readline().strip().split())))
    
    for i in range(9):
        if is_end:
            for j in range(9):
                if is_end:
                    if plate[i][j]:
                        continue

                    for n in range(1, 10):
                        if promise(i, j, n):
                            plate[i][j] = n
                            sdoku(i)
                            plate[i][j] = 0

# st = time.perf_counter()
sol_2580()
# ed = time.perf_counter()
# print(int(round(ed - st))*1000)