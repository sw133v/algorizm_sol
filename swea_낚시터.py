import sys
sys.stdin = open("낚시터 인풋.txt", "r")

def back():
    pass

def solution ():
    big = int(input())
    site = [0] * big
    
    info = {}
    for i in range(3):
        info[i] = list(map(int, input().split()))
    
    gate_order = [
        [0,1,2], [0,2,1], 
        [1,0,2], [1,2,0], 
        [2,0,1], [2,1,0],
        ]
    
    for gate_info in gate_order:
        for i in gate_info:
            print(i, info[i])
    
    # return a
    # print(big)
    # print(1,gate1, g1_person)
    # print(2,gate2, g2_person)
    # print(3,gate3, g3_person)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''
        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    solution()
    # print(solution())
    # ///////////////////////////////////////////////////////////////////////////////////
