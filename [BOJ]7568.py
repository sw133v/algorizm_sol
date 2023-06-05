def sol_7568():
    input_length = int(input())
    input_data = []
    res =''
    for _ in range(input_length):
        input_data.append(list(map(int, input().split())))

    for person1 in input_data:
        count = 1
        for person2 in input_data:
            if person1[0] < person2[0] and person1[1] < person2[1]:
                count += 1
        if res:
            res += f' {count}'
        else:
            res += f'{count}'
    
    print(res)

sol_7568()