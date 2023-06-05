def sol_1181():
    data = set()
    for _ in range(int(input())):
        data.add(input())
    data = list(data)
    data.sort()
    data.sort(key=lambda x:len(x))
    for s in data:
        print(s)

sol_1181()