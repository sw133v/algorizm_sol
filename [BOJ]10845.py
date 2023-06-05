from collections import deque
import sys
def sol_10845():
    queue = deque()
    input_lines = sys.stdin.readlines()

    for i in range(1,int(input_lines[0])+1):
        func = list(input_lines[i].split())
        
        if len(func)-1:
            queue.append(func[1])
        else:
            if func[0] == 'pop':
                if queue:
                    print(queue.popleft())
                else:
                    print(-1)
            
            if func[0] == 'size':
                print(len(queue))
                
            if func[0] == 'empty':
                if len(queue):
                    print(0)
                else:
                    print(1)
                    
            if func[0] == 'front':
                if queue:
                    print(queue[0])
                else:
                    print(-1)
                
            if func[0] == 'back':
                if queue:
                    print(queue[-1])
                else:
                    print(-1)

sol_10845()