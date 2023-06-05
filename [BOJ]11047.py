def sol11047():
    n, money = map(int, input().split())
    coins = []
    for _ in range(n):
        coins.append(int(input()))
    coins.reverse()
    temp_money = money
    res = 0
    for coin in coins:
        if temp_money:
            if temp_money // coin:
                res += temp_money // coin
                temp_money = temp_money % coin
    print(res)

sol11047()