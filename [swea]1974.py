import sys
sys.stdin = open('swea1974_input.txt', 'r')

def sol():
    cont_sort = [0] * 10
    sdoku = [list(map(int, input().split()))for _ in range(9)]
    state = 1

    for row in range(9):
        for col in range(9):
            cont_sort[sdoku[row][col]] += 1
        if 0 in cont_sort[1:]:
            #print(f'1 {cont_sort[1:]}')
            state = 0
            break
        cont_sort = [0] * 10
        if state == 0:
            break

    if state != 0:
        for col in range(9):
            for row in range(9):
                cont_sort[sdoku[row][col]] += 1
            if 0 in cont_sort[1:]:
                state = 0
                #print(f'2 {cont_sort[1:]}')
                break
            cont_sort = [0] * 10
            if state == 0:
                break

    if state != 0:
        srow, scol = 0, 0
        while srow != 6 and scol != 6 and state == 1:
            for row in range(srow, srow+3):
                for col in range(scol, scol+3):
                    cont_sort[sdoku[row][col]] += 1
            if 0 in cont_sort[1:]:
                #print(f'3 {cont_sort[1:]}')
                state = 0
                break
            cont_sort = [0] * 10
            if srow == 6 and scol == 6:
                pass
            else:
                scol += 3
                if scol == 9:
                    scol = 0
                    srow += 3
    return state

T = int(input())
for test_case in range(1, 1+T):
    print(f'#{test_case} {sol()}')