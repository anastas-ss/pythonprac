a = list(eval(input()))
n = len(a)
flag = True
while (flag):
    flag = False
    for i in range(0, n-1):
        if a[i]**2%100 > a[i+1]**2%100:
            a[i], a[i+1] = a[i+1], a[i]
            flag = True
print(a)  
