def func(num):
    if num:
        print(num)
        num-=1
        return func(num)
    else:
        return 0
