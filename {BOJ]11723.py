import sys
def sol11723():
    S = 0
    for _ in range(int(sys.stdin.readline())):
        op = list(sys.stdin.readline().split())
        if op[0] == "add":
            S |= (1 << int(op[1]))
        elif op[0] == "remove":
            S &= ~(1 << int(op[1]))
        elif op[0] == "check":
            if S & (1 << int(op[1])):
                print(1)
            else:
                print(0)
        elif op[0] == "toggle":
            S ^= (1 << int(op[1]))
        elif op[0] == "all":
            S = 2097151
        elif op[0] == "empty":
            S = 0

sol11723()