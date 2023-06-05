def sol_1475():
    def to_half(a, b):
        return (a+b)/2

    def rounds(a):
        if a % 1:
            return int(a+1)
        else:
            return int(a)
    
    num_manu = [0 for _ in range(10)]
    
    for i in input():
        num_manu[int(i)] += 1
    six_or_nine = to_half(num_manu[6], num_manu[9])
    six_or_nine = rounds(six_or_nine)
    num_manu = num_manu[:-1]
    num_manu[6]=(six_or_nine)
    print(max(num_manu))
    
sol_1475()