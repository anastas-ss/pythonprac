box = []
a = eval(input())
box.append(a)
n = len(a)
for i in range (1,n):
	a = eval(input())
	box.append(a)
for i in range (0, n):
	for j in range (0, n):
		print (box[j][i], end=" ")
	print() 
#pprint.pprint(box)
