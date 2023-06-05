def sol_2747():
    # re_data = [0,1].extend([-1]*)
    # def recursion(n):
    #     if len(re_data) > n:
    #         return re_data[n]
    #     else:
    #         pass
    # print(recursion(int(input())))
    in_data = int(input())
    result_list = [0, 1]
    for i in range(2, in_data+1):
        result_list.append(result_list[i-1]+result_list[i-2])
    print(result_list[-1])
    
sol_2747()