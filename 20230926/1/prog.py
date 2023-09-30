M, N =  eval(input())
print(list(i for i in range(M, N) if all (i % j for j in range(2, int(i**(1/2))+1)) and i != 1))


