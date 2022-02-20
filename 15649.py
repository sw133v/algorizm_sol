def my_sum(int_lst):
    total = 0
    for val in int_lst:
        total += val
    return total

def my_len(lst):
    cnt = 0
    for _ in lst:
        cnt += 1
    return cnt

def my_lst_sort(lst):
    print(lst)
    for i in range(my_len(lst) - 1):
        for j in range(i + 1, my_len(lst)):
            if lst[i][0] > lst[j][0]:
                lst[i], lst[j] = lst[j], lst[i]
            elif lst[i][0] == lst[j][0]:
                if lst[i][1] > lst[j][1]:
                    lst[i], lst[j] = lst[j], lst[i]
    print(lst)


def sol(lst):
    b_list = [val for val in range(1, lst[0] + 1)]
    # lst[0] 원소의 갯수 lst[1] 합
    cnt = 0
    res_set = set()
    for i in range(1 << my_len(b_list)):
        k = list()
        for j in range(lst[0]):
            if i & (1 << j):
                k += [b_list[j]]

            if my_len(k) > lst[1]:
                k = []
                break

        if my_len(k) < lst[1]:
            k = []

        #print(k, end=' ')
        if k != []:
            res_set.add(tuple(k))
        res_list = list(res_set)

    print(res_list)
    for val in res_set:
        if my_sum(val) == lst[1]:
            cnt += 1

    return res_list


val_lst = list(map(int, input().split()))
res = sol(val_lst)
k = my_lst_sort(res)

