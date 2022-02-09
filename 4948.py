def my_prime_num(n):
    result = [True] * ((2 * n) + 1)
    result[0], result[1] = False, False

    for i in range(2, 2 * n + 1):
        if result[i] == True:
            for j in range(i + i, 2 * n + 1, i):
                result[j] = False

    cnt = 0
    for i in range(n + 1, 2 * n + 1):
        if result[i] == True:
            cnt += 1
    return cnt


result_lst = []
while True:
    n = int(input())
    if n == 0:
        break
    result_lst += [my_prime_num(n)]

for num in result_lst:
    print(num)