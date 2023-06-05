def sol5525():
    P = 'I'
    for _ in range(int(input())):
        P += 'OI'
    PL = len(P)
    length = int(input())
    check = input().strip('O')
    length = len(check)
    res = 0

    i = 0
    while i < length - PL + 1:
        if check[i:i+PL] == P:
            res += 1
            i += 2
            
        else:
            temp = 0
            for ti in range(PL):
                if check[i+ti] == P[ti]:
                    temp += 1
                else:
                    break
            if temp == 0:
                temp += 1
            i += temp
            
    print(res)

sol5525()