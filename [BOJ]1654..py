def sol_1654():
    my_ea, max_ea = map(int, input().split())
    my_lan_cables = []
    for _ in range(my_ea):
        a = int(input())
        if a:
            my_lan_cables.append(a)
    
    if max_ea == 1:
        print(max(my_lan_cables))
    else:
        max_length = sum(my_lan_cables) // max_ea
        # min_length = sum(my_lan_cables) // (max_ea + my_ea)
        min_length = 1

        pivot = (min_length + max_length) // 2
        res = 0
        while True:
            temp_count = 0
            
            for lan_cable in my_lan_cables:
                temp_count += lan_cable // pivot
            
            if temp_count >= max_ea:
                if max_length - min_length <= 1:
                    res = max_length
                    break
                min_length = pivot
                    
            else:
                if max_length - min_length <= 1:
                    res = min_length
                    break
                max_length = pivot
            
            pivot = (min_length + max_length) // 2 + (min_length + max_length) % 2
        
        print(res)

sol_1654()