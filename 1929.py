'''
def my_prime_num(n, m):
    if m < 2:
        return []
    result_lst = [2]
    
    for num in range(2, m):
        
        for prime_num in result_lst:
            if num % prime_num == 0 :
                break

            elif prime_num == result_lst[-1]:
                result_lst += [num]

    return result_lst

n, m = map(int , input().split())
for i in my_prime_num(n, m):
    print(i)

'''

#print(my_prime_num(n, m))
'''
result = list()
start = n
print(n, m)

if n != 2:
    
'''

#while start <= m:
    
    
'''
def prime_list(n, m):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    if m < 2:
        return []
    sieve = [True] * m

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    k = int(m ** 0.5)
    for i in range(n, k + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, m, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(n, m) if sieve[i] == True]
'''

def my_prime_num1(n, m):
    
    if m < 2:
        return []
    sieve = [True] * m
    
    for i in range(2, m):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, m, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False
    
    return [i for i in range(n, m) if sieve[i] == True]

def my_prime_num(n, m):
    if m < 2:
        return []
    
    result = [True] * (m + 1)
    
    for i in range(2, m + 1):
        if result[i] == True:
            for j in range(i+i, m + 1, i):
                result[j] = False
    
    if n == 1:
        return [i for i in range(2, m + 1) if result[i] == True]
    else :
        return [i for i in range(n, m + 1) if result[i] == True]
    
    
n, m = map(int , input().split())
for i in my_prime_num(n, m):
    print(i)