from collections import defaultdict
def sol1620():
    poket = defaultdict(str)
    n, m = map(int, input().split())
    
    for i in range(1, n+1):
        monster = input()
        poket[i] = monster
        poket[monster] = i
    
    for _ in range(m):
        quest = input()
        if quest.isdigit():
            print(poket[int(quest)])
        else:
            print(poket[quest])
            
sol1620()