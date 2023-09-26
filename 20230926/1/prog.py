M, N =  eval(input())
print(list(i for i in range(N, M+1) if not all (i % j for j in range(2, int(i**(1/2))+1))))

