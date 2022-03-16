def solution(money, costs):
    money_list = [1, 5, 10, 50, 100, 500]
    temp = [(money_list[i] - costs[i])/money_list[i] for i in range(6)]
    print(temp)

    priorty = []
    while len(priorty) < 6:
        for i in range(-1, -7, -1):
            if temp[i] == max(temp):
                priorty += [i]
                temp[i] = min(temp) - 1
                break
    print(priorty)
    answer = 0
    goal = 0
    a = money

    for i in priorty:
        res = a % money_list[i]
        a = a // money_list[i]

        goal += money_list[i] * a
        answer += costs[i] * a
        a = res

    return answer

a = solution(4578, [1, 4, 99, 35, 50, 1000])
print(a)