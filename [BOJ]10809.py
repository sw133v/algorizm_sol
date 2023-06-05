from collections import defaultdict
def sol_10809():
    data = [-1]*26
    alpha = defaultdict(int)
    for i in range(0, 26):
        alpha[chr(i+97)] = i
    
    input_str = input().lower()
    for i in range(len(input_str)):
        if data[alpha[input_str[i]]] == -1:
            data[alpha[input_str[i]]] = i
    
    for a in data:
        print(f'{a}', end=' ')
    
sol_10809()