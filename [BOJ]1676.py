def sol1676():
    def pac(n):
        if n == 0: return 1
        elif n == 1: return 1
        else: return pac(n-1) * n
    res = 0
    data = str(pac(int(input())))
    data = reversed(data)
    for i in data:
        if i == '0':
            res += 1
        else:
            break
    print(res)

sol1676()