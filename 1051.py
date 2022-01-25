def inp_data():
    data = input().split(' ')
    mat = []
    
    for i in range(int(data[0])):
        mat += [input()]
        
    return int(data[0]), int(data[1]), mat

def my_solve():
    row, col, mmat = inp_data()
    if row >= col :
        max = row 
    else :
        max = col
    
    for i in row:
        pass
    pass
    #pass


inp_data()
