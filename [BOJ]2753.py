def sol_2753():
    
    in_data = int(input())
    if (in_data%4 == 0 and in_data%100 != 0)or in_data % 400 == 0:
        return 1
    else:
        return 0

print(sol_2753())