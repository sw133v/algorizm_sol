def sol_11866():
    person, num = map(int, input().split())
    people = [i for i in range(1,person+1)]
    res = []
    
    while people:
        if len(people) >= num:
            people = people[num-1:]+people[:num-1]
            res.append(people.pop(0))
        else:
            for _ in range(num-1):
                people = people[1:]+[people[0]]
            res.append(people.pop(0))
    
    print('<',end='')
    for val in res:
        if val != res[-1]:
            print(f'{val}, ',end='')
        else:
            print(f'{val}>')

sol_11866()