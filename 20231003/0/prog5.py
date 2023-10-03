def lin(a, b):
    return lambda x: a*x + b

f = lin(4, 7)
print(f(5))
