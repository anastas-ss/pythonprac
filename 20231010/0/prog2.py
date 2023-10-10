from decimal import Decimal

def esum(N, one):
	tp = type(one)
	sum = 1
	fac = 1
	for i in range(1, N):
		sum = sum *(1/i)
		
	print(sum)
	print((1+sum)**N)
	return tp((1 + sum)**N)
a, b = eval(input())
print(esum(a, b))
#где-то косяк
