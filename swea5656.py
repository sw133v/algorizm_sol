import sys
sys.stdin = open('swea5656_input.txt', 'r')

def sol():
    N, W, H = map(int, input().split())
    print(N, W, H)

    doll = [list(map(int, input().split())) for _ in range(H)]
    print(doll)

T = int(input())
for test_case in range(1, 1+T):
    print(f'#{test_case} {sol()}')