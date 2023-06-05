def sol_1018():
    def check():
        ref_plate1
        ref_plate2
        n, m = map(int, input().split())
        check_plate = [list(input()) for _ in range(n)]
        max_change = 64
        
        for i in range(0, n-8 +1):
            if max_change == 0:
                break
            
            for j in range(0, m-8 +1):
                temp_max1 = 0
                temp_max2 = 0
                
                for ci in range(i, i+8):
                    for cj in range(j, j+8):
                        if ref_plate1[ci-i][cj-j] != check_plate[ci][cj]:
                            temp_max1 += 1
                        if ref_plate2[ci-i][cj-j] != check_plate[ci][cj]:
                            temp_max2 += 1

                if min(temp_max1, temp_max2) < max_change:
                    max_change = min(temp_max1, temp_max2)
                if max_change == 0:
                    break
        print(max_change)
        
    ref_plate1 = []
    ref_plate2 = []
    for _ in range(4):
        ref_plate1.append(["W","B","W","B","W","B","W","B"])
        ref_plate1.append(["B","W","B","W","B","W","B","W"])    
    for _ in range(4):
        ref_plate2.append(["B","W","B","W","B","W","B","W"])
        ref_plate2.append(["W","B","W","B","W","B","W","B"])
    
    check()
    
sol_1018()