a, b, c = eval(input())
print(not min(a, b, c, 0) and 2 * max(a, b, c) < a + b + c)
