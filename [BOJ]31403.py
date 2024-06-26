import sys

def sol_31403():
    data = []
    for _ in range(3):
        data.append(int(sys.stdin.readline()))
    print(data[0]+data[1]-data[2])
    print(int(str(data[0])+str(data[1]))-data[2])

sol_31403()