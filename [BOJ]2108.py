from collections import defaultdict
def sol_2108():
    input_length = int(input())
    count = defaultdict(int)
    input_data = []
    minus = 0
    for _ in range(input_length):
        temp_data = int(input())
        count[temp_data] += 1
        input_data.append(temp_data)
    input_data.sort()
    
    avg = sum(input_data) / input_length
    if avg < 0:
        minus = 1
        avg *= -1
    
    if avg-int(avg) > 0.5:
        avg = int(avg) + 1
    else:
        avg = int(avg)
    
    if minus:
        avg *= -1
        
    new_count = {k: v for k, v in count.items() if v == max(count.values())}
    temp_third_andswer = sorted(new_count)
    
    print(avg)
    print(input_data[input_length//2])
    if len(temp_third_andswer) - 1:
        print(temp_third_andswer[1])
    else:
        print(temp_third_andswer[0])
    print(max(input_data) - min(input_data))

sol_2108()