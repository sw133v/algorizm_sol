import sys
sys.stdin = open('swea_13994_input.txt', 'r')

def sol():
    bus = int(input())
    bus_info = [list(map(int, input().split())) for _ in range(bus)]
    pass

T = int(input())
for test_case in range(1, 1+T):
    print(f'#{test_case} {sol()}')