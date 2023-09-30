A = []
B = []
a = eval(input())
n = len(a)
A.append(a)
for i in range (2, n*2+1):
    if i <= n:
        a = eval(input())
        A.append(a)
    else:
        b = eval(input())
        B.append(b)
for iA in range(0,n):
    for jB in range(0,n):
        P = 0
        for j in range(0, n):
            P += A[iA][j]*B[j][jB]
        if jB == n-1:
            print(P, end="")
        else:
            print(P, end=",")
    print()

