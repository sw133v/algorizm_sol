def sol_sub():
    pass

def solution(n, clockwise):
    answer = [[0] * n for _ in range(n)]
    if clockwise:
        delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    else:
        delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    soonser = [[0, 0], [0, n - 1], [n - 1, n - 1], [n - 1, 0]]

    for i in soonser:
        row = i[0]
        col = i[1]
        re = n - 1
        val = 2
        answer[row][col] = 1
        k = 0
        while True:
            if k == 0:
                for _ in range(re-1):
                    row += delta[k % 4][0]
                    col += delta[k % 4][1]
                    answer[row][col] = val
                    print(val)
                    val += 1
            else:
                for _ in range(re):
                    row += delta[k % 4][0]
                    col += delta[k % 4][1]
                    answer[row][col] = val
                    print(val)
                    val += 1

            k += 1
            if re == 1:
                break
            elif re == 2:
                re -= 1
            else:
                re -= 2
        print(answer)

        if clockwise:
            a = delta.pop(0)
            delta += [a]
        else:
            a = delta.pop(-1)
            delta = [a] + delta

    return answer


a = solution(5, True)
for i in range(5):
    print(a[i])
#print(solution(6, False))
#print(solution(9, False))