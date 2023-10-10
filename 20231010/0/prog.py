from decimal import Decimal
def multiplier(x, y, type):
	return type(x)*type(y)
print(multiplier(input(), input(), int))
