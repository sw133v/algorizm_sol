def sol_5988():
    lenth = int(input())
    input_list = list()
    for i in range(lenth):
        input_list.append(int(input()))
    
    for data in input_list:
        if data % 2 == 0:
            print("even")
        else:
            print("odd")

sol_5988()