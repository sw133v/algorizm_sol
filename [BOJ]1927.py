import sys

def sol_1927():
    def valueSwap(big, small):
        temp_data = min_heap[big]
        min_heap[big] = min_heap[small]
        min_heap[small] = temp_data
    def upSwap():
        global heap_len
        point = (heap_len - 1)
        
        while point > 0:
            parent = (point - 1) // 2
            if min_heap[point] >= min_heap[parent]:
                break
            valueSwap(parent, point)
            point = parent
    
    def downSwap():
        global heap_len
        point = 0
        while True:
            son2 = (point + 1) * 2
            son1 = son2 - 1
            
            if heap_len <= son1:
                break
            
            elif heap_len <= son2:
                if min_heap[point] > min_heap[son1]:
                    valueSwap(point, son1)
                    point = son1
                else:
                    break
            
            elif min_heap[point] < min_heap[son1] and min_heap[point] < min_heap[son2]:
                break

            else:                
                if min_heap[son1] < min_heap[son2]:
                    valueSwap(point, son1)
                    point = son1
                else:
                    valueSwap(point, son2)
                    point = son2 

        # if heap_len > (point + 1) * 2:
        #     # 자식 노드랑 비교
        #     pass
        # else:
        #     pass
    
    def heapAppend(num):
        global heap_len
        heap_len += 1
        min_heap.append(num)
        upSwap()
    
    def heapDel():
        global heap_len
        if heap_len > 1:
            print(min_heap[0])
            min_heap[0] = min_heap[-1]
            min_heap.pop(-1)
            heap_len -= 1
            downSwap()
        elif heap_len == 1:
            print(min_heap.pop(0))
            heap_len -= 1
        else:
            print(0)

    min_heap = []
    n = int(sys.stdin.readline())
    
    for _ in range(n):
        num = int(sys.stdin.readline())
        if num == 0:
            heapDel()
        else:
            heapAppend(num)
        
heap_len = 0
sol_1927()