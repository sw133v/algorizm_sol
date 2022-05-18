def solution(new_id):
    a = new_id
    a= a.lower()
    a = list(map(str, a))

    alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','.','-','_']
    idx = 0
    
    while True:
        if idx == len(a):
            break
        if a[idx] in alph:
            idx += 1
            continue
        else:
            a.pop(idx)
    idx = 0
    while True:
        if idx == len(a)-1:
            break
        if a[idx]+a[idx+1] == '..':
            a.pop(idx)
            continue
        idx += 1
    
    if a[0] == '.':
        a.pop(0)
        
    if len(a) >= 16:
        a = a[:15]
    
    if a:
        if a[-1] == '.':
            a.pop()
        
    a = ''.join(a)
    if len(a) == 0:
        return 'aaa'
    while len(a)<3:
            a += a[-1]
    
    print(a)
    print(len(a))
    
    answer = ''
    return a