from collections import defaultdict
def sol_18111():
    y, x, had_block = map(int, input().split())
    floors = defaultdict(int)
    for _ in range(y):
        for i in list(map(int, input().split())):
            floors[i] += 1
            
    h = max(floors)
    l = min(floors)
    
    res = [] # [높이, 시간]순으로 짠다
             # 높이를 기준으로 정렬을 한 후에 출력
             
    for i in range(l, h+1):
        need_block = had_block
        time = 0
        
        for j in list(floors):
            if i > j: # 쌓는거 1초
                gap = i -j
                temp = gap * floors[j]
                time += temp
                need_block -= temp
            else: # 파는거 2초
                gap = j - i
                temp = gap * floors[j]
                time += temp*2
                need_block += temp
                
        if need_block > -1:
            if res:
                if res[0][1] > time:
                    res = [[i, time]]
                elif res[0][1] == time:
                    res.append([i, time])
            else:
                res.append([i, time])
                
    res.sort(key=lambda x: x[1])
    res.reverse()
    print(res[0][1], res[0][0])
                
sol_18111()

    # 파는건 2초 쌓는건 1초
    # for i in range(l, h+1):
    #     need_block = had_block
    #     time = 0
    #     for floor in floors:
    #         block = [b for b in floor if b != i]
    #         for b in block:
    #             if b > i:
    #                 a = b - i
    #                 time += a*2
    #                 need_block += a
    #             else:
    #                 a = i - b
    #                 time += a
    #                 need_block -= a
                    
    #     if need_block > -1:
    #         if res:
    #             if res[0][1] > time:
    #                 res = [[i, time]]
    #             elif res[0][1] == time:
    #                 res.append([i, time])
    #         else:
    #             res.append([i, time])
                
    # res.sort(key=lambda x: x[1])
    # res.reverse()
    # print(res[0][1], res[0][0])