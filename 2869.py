a, n, v = [x for x in map(int,input().split())]
if a >= v:
    print(1)
print((v-a) // (a-n) + 2) if (v-a) < (a-n) else print((v-a) // (a-n) + 1)