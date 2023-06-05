def sol_2805():
    N, M = map(int, input().split())
    tree_list = list(map(int, input().split()))
    
    min_H = 0
    max_H = max(tree_list)
    pivot = (min_H + max_H) // 2
    leftover = [sum(tree_list), min_H]
    
    while max_H - min_H > 1:
        temp_data = 0
        for tree in tree_list:
            take_tree = tree - pivot
            if take_tree > 0:
                temp_data += take_tree

        if temp_data < M:
            max_H = pivot
            
        else:
            if leftover[0] == temp_data and leftover[1] < pivot:
                leftover[1] = pivot
            elif leftover[0] > temp_data - M:
                leftover[0] = temp_data - M
                leftover[1] = pivot
            min_H = pivot
        
        pivot = (min_H + max_H) // 2
        
    print(leftover[1])

sol_2805()
