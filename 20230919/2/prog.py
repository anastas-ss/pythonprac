sum = 0
while (a := eval(input())) > 0:
	sum+=a
	if sum > 21:
		print (sum)
		break
else:
	print (a)

