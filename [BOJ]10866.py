from collections import deque
def sol_10866():
    res = deque()
    ans = []
    for _ in range(int(input())):
        input_data = input().split(' ')
        if len(input_data)-1:
            if len(input_data[0])-9:
                res.appendleft(int(input_data[1]))
            else:
                res.append(int(input_data[1]))
            continue
        else:
            input_data = str(*input_data).split('_')
            if len(input_data)-1:
                if len(input_data[1])-4:
                    if res:
                        # print(res.popleft())
                        ans.append(res.popleft())
                    else:
                        # print(-1)
                        ans.append(-1)
                else:
                    if res:
                        # print(res.pop())
                        ans.append(res.pop())
                    else:
                        # print(-1)
                        ans.append(-1)
                continue
            else:
                if input_data[0] == 'size':
                    # print(len(res))
                    ans.append(len(res))
                elif input_data[0] == 'empty':
                    if res:
                        # print(0)
                        ans.append(0)
                    else:
                        # print(1)
                        ans.append(1)
                elif input_data[0] == 'front':
                    if res:
                        # print(res[0])
                        ans.append(res[0])
                    else:
                        # print(-1)
                        ans.append(-1)
                elif input_data[0] == 'back':
                    if res:
                        # print(res[-1])
                        ans.append(res[-1])
                    else:
                        # print(-1)
                        ans.append(-1)
    for a in ans:
        print(a)

sol_10866()