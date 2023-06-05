'''
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.

출력
첫째 줄에 N!을 출력한다.
'''
def sol_10872():
    def recursion(n):
        ans = n
        if n == 0:
            return 1
        return ans * recursion(n-1)
    print(recursion(int(input())))

sol_10872()