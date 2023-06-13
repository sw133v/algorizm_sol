import sys

def sol_14888():
    def backTracking(deep):
        nonlocal big_res, sm_res, op, temp_res

        if deep == gaesu:
            val = althi_op()
            if val > big_res:
                big_res = val
            if val < sm_res:
                sm_res = val
            return
        
        for i in range(4):
            if op[i]:
                op[i] -= 1
                temp_res.append(i)
                backTracking(deep + 1)
                op[i] += 1
                temp_res.pop(-1)

    def althi_op():
        """
        0 는 +, 1 는 -, 2 는 *, 3 는 /
        """
        temp = num_list[0]
        for i in range(gaesu-1):
            if temp_res[i] == 0:
                temp += num_list[i+1]
            elif temp_res[i] == 1:
                temp -= num_list[i+1]
            elif temp_res[i] == 2:
                temp *= num_list[i+1]
            elif temp_res[i] == 3:
                if temp < 0:
                    temp = (-temp // num_list[i+1]) * -1
                else:
                    temp = temp // num_list[i+1]
        return temp

    gaesu = int(sys.stdin.readline())
    num_list = list(map(int, sys.stdin.readline().split()))
    op = list(map(int, sys.stdin.readline().split()))
    temp_res = []
    big_res = -1000000001
    sm_res = 1000000001
    
    for i in range(4):
        if op[i]:
            op[i] -= 1
            temp_res.append(i)
            backTracking(2)
            op[i] += 1
            temp_res.pop(-1)
    
    print(big_res)
    print(sm_res)

sol_14888()