from math import *
def Calc(s, t ,u):
    ss =lambda x: eval(s)
    tt = lambda x: eval(t)
    uu = lambda x,y: eval(u)
    return lambda x: uu(ss(x), tt(x))
s, t, u = eval(input())
x = eval(input())
F = Calc(s, t, u)
print(F(x))
