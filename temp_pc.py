from collections import deque
class my_heap():
    def __init__(self):
        self.index = 1
        self.data = deque(int)
        self.data.append(None)

    def check(self):
        if self.data[0]:
            return 1
        return 0

    def h_append(self, val):
        if self.check():
            self.data.append(None)
        self.data[self.index] = val
        temp = self.index
        self.index += 1
        while temp:
            if self.data[temp] < self.data[(temp // 2)]:
                t = self.data[temp]
                self.data[temp] = self.data[(temp // 2)]
                self.data[(temp // 2)] = t
            else:
                break

    def h_pop(self):
        res = self.data[1]
        self.data[1] = self.data[self.index]
        
        return res

def sol1927():
    pass

sol1927()