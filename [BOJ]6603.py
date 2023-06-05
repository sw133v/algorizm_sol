def sol_6603():
    while True:
        num_list = list(map(int, input().split()))
        if len(num_list) < 2:
            break
        length = num_list[0]
        num_list = num_list[1:]
        num_list.sort()
        
        res = set()
        
        for first in range(length-5):
            for second in range(first+1,length-4):
                for third in range(second+1,length-3):
                    for forth in range(third+1,length-2):
                        for fifth in range(forth+1,length-1):
                            for sixth in range(fifth+1,length):
                                temp_data = []
                                temp_data.append(num_list[first])
                                temp_data.append(num_list[second])
                                temp_data.append(num_list[third])
                                temp_data.append(num_list[forth])
                                temp_data.append(num_list[fifth])
                                temp_data.append(num_list[sixth])
                                res.add(tuple(temp_data))
        res = list(res)
        res.sort()
        for i in res:
            print(*list(i))
            
        print()

sol_6603()