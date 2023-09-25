a = eval(input())
i = j = a
while i <= a + 2:
    while j <= a + 2:
        pr = i*j
        sum = 0
        while pr:
            sum+=pr%10
            pr = pr//10
        if sum == 6:
            pr = ':=)'
        else:
            pr = i*j
        if j == a + 2:
            print (i, "*", j, "=", pr)
        else:
            print (i, "*", j, "=", pr, end=" ")
        j+=1
    j-=3
    i+=1
    
