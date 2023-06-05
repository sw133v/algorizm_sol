from collections import defaultdict
def sol_9012():
    def is_equal():
        def is_fine(str_data):
            data = list(str_data)
            is_true = 0
            res = ''
            if data.pop(0) == '(':
                is_true += 1
            else:
                is_true -= 1
            
            if is_true == -1:
                return 'NO'
            
            while data:
                if data.pop(0) == '(':
                    is_true += 1
                else:
                    is_true -= 1
                if is_true < 0:
                    res = 'NO'
                    break
            if res == '':
                res = 'YES'
            return res
            
            
        bracket = defaultdict(int)
        input_data = input()
        for i in input_data:
            bracket[i] += 1
        if bracket['('] - bracket[')'] != 0:
            return "NO"
        else:
            return is_fine(input_data)
        
    ans = []
    for _ in range(int(input())):
        ans.append(is_equal())
        
    for res in ans:
        print(res)

sol_9012()