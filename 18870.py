
'''
def inp_data():
    num = int(sys.stdin.readline())
    lst = [int (i) for i in sys.stdin.readline().split()]
    return lst


def make_set(num_list):
    result_set = set()
    for i in num_list:
        result_set.add(i)
    return result_set

def sol(rset, num_list):
    result_list = list()
    for i in num_list:
        cnt = 0
        for j in rset:
            if i > j :
                cnt += 1
        print(f'{cnt}',end=' ')
'''
        
'''
    for i in result_list:
        print(f'{i}', end=' ')
'''

    
# set으로 중복을 제거하고
# 해당 리스트를 중복제거된값 set을 시퀀스 스럽게 비교를 하여 값을 리턴 시키면 될듯?
'''
lst = inp_data()
num_set = make_set(lst)
sol(num_set, lst)
'''
    #o = Oeesz(n, lst)
    #o.make_set()
    #o.sol()

'''
num = int(sys.stdin.readline())
lst = [int (i) for i in sys.stdin.readline().split()]

result_set = set()
for i in range(num):
    result_set.add(lst[i])

result_list = list()
for i in lst:
    cnt = 0
    for j in result_set:
        if i > j :
            cnt += 1
    print(f'{cnt}',end=' ')
    
'''
'''
import sys

N=int(sys.stdin.readline())

num=list(map(int,sys.stdin.readline().split()))

s_num=list(set(num))

for i in num:

    print(s_num.index(i),end=' '
    '''
    
    
'''
    for i in self.list:
        cnt = 0
        for j in self.nojoongset:
            if i > j :
                cnt += 1
        self.resultlist += [cnt]
    for i in self.resultlist:
        print(f'{i}', end=' ')
'''

'''
class Oeesz():
    
    def __init__(self, n, args):
        self.len = n
        self.list = args
        self.nojoongset = dict()
        
    def sol(self):
        
        k = sorted(self.list)
        for i in range(len(k)):
            if (k[i] in self.nojoongset) == False:
                self.nojoongset[k[i]] = i
        
        self.resultlst = list()
        for i in self.list:
            print(self.nojoongset[i], end=' ')

n=int(sys.stdin.readline())
num=list(map(int,sys.stdin.readline().split()))
o = Oeesz(n, num)
o.sol()
'''

import sys
n=int(sys.stdin.readline())
num=list(map(int,sys.stdin.readline().split()))
    
nojoongset = dict()
k = sorted(num)
c = 0
for i in range(n):
    if (k[i] in nojoongset) == False:
        nojoongset[k[i]] = c
        c += 1

resultlst = list()
for i in num:
    print(nojoongset[i], end=' ')