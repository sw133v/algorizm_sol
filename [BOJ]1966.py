from collections import deque
def sol_1966():
    def sol_sub_1966():
        length, des_index = map(int, input().split())
        data = deque(list(map(int, input().split())))
        max_data = max(data)
        count = 1
        while data:
            if data[0] == max_data:
                if des_index == 0:
                    break
                
                data.popleft()
                max_data = max(data)
                count += 1

            else:
                k = data.popleft()
                data.append(k)
            
            if des_index:
                des_index -= 1
            else:
                des_index = len(data)-1

        print(count)

    
    input_length = int(input())
    for _ in range(input_length):
        sol_sub_1966()

sol_1966()

        # if length-1:
        #     how_many = data.count(des_data)
        #     if data_max_data == des_data:
        #         if how_many-1:
        #             count = 1
        #             for i in range(0, des_index):
        #                 if data[i] == data_max_data:
        #                     count +=1
        #             print(count)
        #             return

        #         else:
        #             print(1)
        #             return

        #     else:
        #         count = len([a for a in data if a > data_max_data])
        #         if how_many-1:
        #             count += len([data[a] for a in range(des_index) if data[a] == des_data])
        #             print(count+1)
        #             return
        #         else:
        #             print(count+1)
        #             return

        # else:
        #     print(1)
        #     return