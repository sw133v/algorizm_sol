def sol_5052():
    def sol_sub():
        res = True
        num_list = []
        for _ in range(int(input())):
            num_list.append(input())
        num_list.sort(key=lambda x:len(x))
        
        for i in range(len(num_list)-1):
            if res:
                for j in range(i+1,len(num_list)):
                    if num_list[i] in num_list[j]:
                        res = False
                        break
            else:
                break
        if res:
            print('YES')
        else:
            print('NO')
    
    for _ in range(int(input())):
        sol_sub()

sol_5052()