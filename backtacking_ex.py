# def backtracking(lev):
#
#     # print(n, end=' ')
#     # if n == 17:
#     #     return
#     # if n != 13:
#     #     print(n, end=' ')
#
#     # backtracking(n + 2)
#     # if n != 13:
#     #     print(n, end=' ')
#     if lev == 3:
#         for i in range(lev):
#             print(path_arr[i], end='')
#         print()
#         return
#
#     for i in range(6):
#         path_arr[lev] = i + 1
#         backtracking(lev + 1)
#         path_arr[lev] = 0
#

# def ju(n, sum):
#
#     if sum > 10:
#         return
#
#     if n == 3:
#         for i in range(n):
#             print(path_arr[i], end='')
#         print(f'들의 합은 {sum}')
#         return
#
#     for i in range(6):
#         path_arr[n] = i+1
#         ju(n + 1, sum + i + 1)
#         path_arr[n] = 0
#
#
# path_arr = [0] * 4
# ju(0, 0)
path = [0] * 10
n = 3
def bbq(lev, sum):



    if lev == n:
        for i in range(lev):
            print(path[i], end='')
        print(f'={sum}')
        return

    for i in range(6):
        path[lev] = i+1
        bbq(lev + 1, sum +i+1)
        path[lev] = 0

bbq(0, 0)
