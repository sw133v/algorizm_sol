def my_len(list):
    cnt = 0
    for i in list:
        cnt += 1
    return cnt

def inp_data():
    data = input().split(' ')
    mat = []
    
    for i in range(int(data[0])):
        mat += [input()]
        
    return int(data[0]), int(data[1]), mat

def my_solve():
    row, col, mmat = inp_data()
    if row > col :
        max = col 
    elif row <= col:
        max = row
    
    result = None
    
    while True:
        if result != None:
            break
        for r in range(row):
            if result != None:
                break
            if r + max > row:
                max -= 1
                break
            for c in range(col):
                if c + max > col:
                    break
                else :
                    if mmat[r][c] == mmat[r][c+max-1] and mmat[r][c] == mmat[r+max-1][c] and mmat[r+max-1][c+max-1] == mmat[r+max-1][c]:
                        result = max
                        break
    return result ** 2

print(my_solve())
    #pass


#inp_data()