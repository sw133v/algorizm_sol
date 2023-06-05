def sol_2941():
    ca_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']
    n = input()
    ans = 0
    n_len = len(n)
    for ca in ca_list:
        ans += n.count(ca)
    ans = n_len - ans
    print(ans)

sol_2941()