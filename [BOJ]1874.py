def sol_1874():
    length = int(input())
    stack = []
    input_data = []
    res = ''
    for _ in range(length):
        input_data.append(int(input()))
    
    index = 1
    while index < length+1:
        stack.append(index)
        res += '+'
        if input_data[0] == stack[-1]:
            while True:
                if (input_data and stack) and input_data[0] == stack[-1]:
                    input_data.pop(0)
                    stack.pop(-1)
                    res += '-'
                else:
                    break
        index += 1
    
    if stack:
        print('NO')
    else:
        for s in res:
            print(s)
    
    pass

sol_1874()