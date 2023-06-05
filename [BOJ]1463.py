import sys

def sol_1463():
    input_data = int(sys.stdin.readline())
    dp_table = [None for _ in range(1000001)]
    init_data = [0, 1, 1]
    for i in range(3):
        dp_table[1 + i] = init_data[i]
    
    for i in range(4, input_data+1):
        dp_table[i] = 1 + min([dp_table[i-1], dp_table[i // 3] + i % 3, dp_table[i // 2] + i % 2])
        
    print(dp_table[input_data])

sol_1463()
