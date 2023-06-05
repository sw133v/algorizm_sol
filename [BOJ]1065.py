'''
문제
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

입력
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

출력
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.
'''
def sol_1065():
    def sol_1065_sub(n):
        data = str(n)
        ans = True
        remainder = int(data[1]) - int(data[0])
        for i in range(1, len(data)-1):
            if int(data[i+1]) - int(data[i]) != remainder:
                ans = False
                break
        return ans
        
    ans = 99
    n = int(input())
    if n <= 99:
        print(n)
    else:
        for i in range(100,n+1):
            if sol_1065_sub(i):
                ans += 1
        print(ans)

sol_1065()