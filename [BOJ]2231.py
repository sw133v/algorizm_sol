def sol_2231():
    num_str = input()
    num_len = len(num_str)
    num = int(num_str)
    
    min_num = num - num_len*9
    if min_num < 0:
        min_num = 0
    ans = 0
    while ans == 0 and min_num <= num:
        if min_num + sum(list(map(int, str(min_num)))) == num:
            ans = min_num
        min_num += 1
    print(ans)

sol_2231()