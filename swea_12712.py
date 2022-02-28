import sys
sys.stdin = open('swea_12712_input.txt', 'r')

# def sol_sub_diagnol(mat, splen):
#     dir = {0: [1, 1],
#            1: [1, -1],
#            2: [-1, 1],
#            3: [-1, -1],
#            }
#     pass

# def sol_sub_RDLU():
#     dir()
#     pass

def sol():
    mat_spray = list(map(int, input().split()))
    mat = [list(map(int, input().split())) for _ in range(mat_spray[0])]
    max_value = mat[0][0]

    for row in range(mat_spray[0]):
        for col in range(mat_spray[0]):
            temp_max = mat[0][0]



T = int(input())
for test_case in range(1, 1+T):
    print(f'#{test_case} {sol()}')