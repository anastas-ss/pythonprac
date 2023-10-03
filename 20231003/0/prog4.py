def sup(f, g):
	return lambda x: f(x)+g(x)
boo = sup(bin, str)
print(boo(5))
