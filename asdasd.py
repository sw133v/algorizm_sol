from collections import deque
MOD = 1234567891
def sol():
    def sub(a, n):
        return (ord(a) - 96) * (31 ** n)

    length = int(input())
    word = input()
    res = 0
    
    for i in range(length):
        res += sub(word[i], i)
    
    print(res % MOD)

sol()