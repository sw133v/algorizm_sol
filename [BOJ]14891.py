import sys
sys.stdin = open('[BOJ]14891.txt', 'r')

def sol():
    # S 가 1 N이 0
    gear1 = input()
    gear2 = input()
    gear3 = input()
    gear4 = input()

    #           0
    #       7       1
    #   6               2
    #       5       3
    #           4
    # 기어 인덱스

    # ex 기어1의 2번 자리와 기어2의 6번 자리가 같다면 가만히 있고
    # 다르다면 기어1이 반시계로 돌때 기어2는 시계로 기어1이 시계로 돌면 기어2는 반시계 방향으로 돈다?
    # 

    goolim = int(input())
    movement = [list(map(int, input().split())) for _ in range(goolim)]

sol()