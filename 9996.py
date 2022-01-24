def is_equal(stls, lst):
    rlst = []       #반환시킬 결과 리스트 변수
    clst = []       #lst내부의 리스트의 길이측정을 위한 변수
    ccnt = 1        #stls의 갯수의 최대값
    
    # clst 를 구하는 코드 ------------------
    for i in lst:
        cnt = -1
        for j in i:
            cnt += 1
        clst += [cnt]
    # --------------------------------------
        
    for i in stls:
        ccnt += 1
    print(len(stls))
    #리스트의 길이가 끝인지 알기위한 ck 변수
    #ck = 0 
    for i in lst:
        result = False
        
    #해당 인자들이 다 들어 갔는지 여부를 조사하는 k 변수 
        k = 0
    #첫글자가 다르면 당연히 패턴이 일치하지 않으므로 결과를 False를 결과값에 전달
        if stls[0] != i[0]:
            result = False
            
        else :
            for j in i:
                if k == ccnt - 1 and j == stls[k] and i.index(j) == clst[k]:
                    result = True
                elif k < ccnt - 1:
                    if stls[k] == j:
                        k += 1

                print(j, k)
        print(result)
        #반환값으로 쓸 result를 rlst에 합연산
        if result == True:
            rlst += ['DA']
        elif result == False:
            rlst += ['NE']
    
    return rlst


how_many = int(input())
stls = input().split('*')

lst = []
for i in range(how_many):
    lst += [input()]

result = is_equal(stls, lst)

for i in result:
    print(i)