import sys
sys.stdin = open('2615_input.txt', 'r')

def lst_cnt(str, lst):
    cnt = 0
    for val in lst:
        if val == str:
            cnt += 1
    return cnt

def sol():
    omock = []
    p1 = 0
    p2 = 0
    res_row = 0
    res_col = 0
    omock += [input().split() for _ in range(19)]

    for row in range(19):
        for col in range(19):
            if omock[row][col] == '1' or omock[row][col] == '2':

                if col+4 < 19: # 오른쪽으로 검사
                    right = [omock[row][col+i] for i in range(1, 5)]
                    if lst_cnt(omock[row][col], right) == 4:
                        if omock[row][col] == '1':
                            p1 = 1
                            res_row = row
                            res_col = col
                            if col+5 < 19:
                                if omock[row][col+5] == '1':
                                    p1 = 0
                                    res_row = 0
                                    res_col = 0
                                if col-1 > -1 and omock[row-1][col - 1] == '1':
                                    p1 = 0
                                    res_row = 0
                                    res_col = 0

                        elif omock[row][col] == '2':
                            p2 = 2
                            res_row = row
                            res_col = col
                            if col + 5 < 19:
                                if omock[row][col + 5] == '2':
                                    p2 = 0
                                    res_row = 0
                                    res_col = 0
                                if col-1 > -1 and omock[row][col - 1] == '2':
                                    p2 = 0
                                    res_row = 0
                                    res_col = 0

                if row+4 < 19: # 아래쪽
                    down = [omock[row+i][col] for i in range(1, 5)]
                    if lst_cnt(omock[row][col], down) == 4:
                        if omock[row][col] == '1':
                            p1 = 1
                            res_row = row
                            res_col = col
                            if row + 5 < 19:
                                if omock[row+5][col] == '1':
                                    p1 = 0
                                    res_row = 0
                                    res_col = 0
                                if row - 1 > -1 and omock[row-1][col] == '1':
                                    p1 = 0
                                    res_row = 0
                                    res_col = 0

                        elif omock[row][col] == '2':
                            p2 = 2
                            res_row = row
                            res_col = col
                            if row + 5 < 19:
                                if omock[row+5][col] == '2' or omock[row-1][col] == '2':
                                    p2 = 0
                                    res_row = 0
                                    res_col = 0
                                if row - 1 > -1 and omock[row-1][col] == '2':
                                    p2 = 0
                                    res_row = 0
                                    res_col = 0


                if row+4 < 19 and col+4 < 19: #우측 사선
                    diagnol = [omock[row+i][col+i] for i in range(1, 5)]
                    if lst_cnt(omock[row][col], diagnol) == 4:
                        if omock[row][col] == '1':
                            p1 = 1
                            res_row = row
                            res_col = col
                            if row + 5 < 19 and col + 5 < 19:
                                if omock[row+5][col + 5] == '1':
                                    p1 = 0
                                    res_row = 0
                                    res_col = 0
                                if row - 1 > -1 and col-1 > -1 and omock[row-1][col-1] == '1':
                                    p1 = 0
                                    res_row = 0
                                    res_col = 0

                        elif omock[row][col] == '2':
                            p2 = 2
                            res_row = row
                            res_col = col
                            if row + 5 < 19 and col + 5 < 19:
                                if omock[row+5][col + 5] == '2' or omock[row-1][col-1] == '2':
                                    p2 = 0
                                    res_row = 0
                                    res_col = 0
                                if row - 1 > -1 and col-1 > -1 and omock[row-1][col-1] == '2':
                                    p2 = 0
                                    res_row = 0
                                    res_col = 0

                if row + 4 < 19 and col - 4 > -1: # 좌측 사선
                    rdiagnol = [omock[row + i][col - i] for i in range(1, 5)]
                    if lst_cnt(omock[row][col], rdiagnol) == 4:
                        if omock[row][col] == '1':
                            p1 = 1
                            res_row = row
                            res_col = col
                            if row + 5 < 19 and col - 5 > -1:
                                if omock[row + 5][col - 5] == '1':
                                    p1 = 0
                                    res_row = 0
                                    res_col = 0
                                if row - 1 > -1 and col+1 > 19 and omock[row-1][col+1] == '1':
                                    p1 = 0
                                    res_row = 0
                                    res_col = 0

                        elif omock[row][col] == '2':
                            p2 = 2
                            res_row = row
                            res_col = col
                            if row + 5 < 19 and col - 5 > -1:
                                if omock[row + 5][col - 5] == '2':
                                    p2 = 0
                                    res_row = 0
                                    res_col = 0
                                if row - 1 > -1 and col+1 > 19 and omock[row-1][col+1] == '2':
                                    p2 = 0
                                    res_row = 0
                                    res_col = 0
    if p1:
        if p2:
            print(0)
        else:
            print(p1)
            print(f'{res_row+1} {res_col+1}')
            return
    elif p2:
        print(p1)
        print(f'{res_row+1} {res_col+1}')
        return

sol()