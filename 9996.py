#입력단 함수
def inp_list():
    ip_num = int(input())
    cpat = input().split('*')

    ip_list = []
    for i in range(ip_num):
        ip_list += [input()]
    
    return ip_list, cpat

#리스트 길이 반환 함수
def my_len(list):
    cnt = 0
    for i in list:
        cnt += 1
    return cnt

#해당 알고리즘
def func_nnns():
    
    #입력단 함수반환값으로 각 변수 초기화 및 빈 리스트 변수 생성
    str_list, pat = inp_list()
    result_lst = []
    
    for i in str_list:

        result = False
        #패턴의 문자열 갯수보다 작으면 요구사항에 맞지 않으므로 결과값을 False로 할당 -- 이부분은 도움받음
        if my_len(i) < my_len(pat[0]) + my_len(pat[1]):
            result = False
        
        #패턴의 문자열 보다 같거나 크면 요구사항에 만족
        elif my_len(i) >= my_len(pat[0] + pat[1]):
            
            #앞의 패턴과 i문자열의 슬라이스를 비교 같지않을시 결과값 False 할당
            if i[:my_len(pat[0])] != pat[0]:
                result = False
            
            #뒤의 패턴과 i문자열의 슬라이스를 비교 같지않을시 결과값 False 할당
            elif i[-my_len(pat[1])::1] != pat[1]:
                result = False
            
            #이외의 모든 결과는 참
            else :
                result = True

        if result == True:
            result_lst += ['DA']
        elif result == False:
            result_lst += ['NE']
    
    for i in result_lst:
        print(i)
    return result_lst

func_nnns()