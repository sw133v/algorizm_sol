class Tsfz:
    
    def __init__(self):
        self.relst = None
        self.low_num = None
        self.high_num = None
        self.input_lst = []
        self.result_lst = []

    def input_data(self):
        
        for i in range(int(input())):
            self.input_lst += [int(input())]
        
        print(self.input_lst)
            
    def solve(self):
        for j in range(len(self.input_lst)):
            for i in range(len(self.input_lst)):
                if i < len(self.input_lst) - 1:
                    if self.input_lst[i] > self.input_lst[i + 1]:
                        self.input_lst[i], self.input_lst[i + 1] = self.input_lst[i + 1], self.input_lst[i]
            print(self.input_lst)

                    
        for i in self.input_lst:
            print(i)

tins = Tsfz()
tins.input_data()
tins.solve()