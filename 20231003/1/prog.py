def Pareto(*args):
    a = []
    for i in range(len(args)):
        flag = True
        for j in range(len(args)):
            if args[i][0] <= args[j][0] and args[i][1] <= args[j][1]:
                if args[i][0] < args[j][0] or args[i][1] < args[j][1]:
                    flag = False
                    break
        if flag:
            a.append(args[i])
    return tuple(a) 

args = eval(input())
print(Pareto(*args))
