from math import sin

def scale(a, b, A, B, x):
        return (x-a)*(B-A)/(b-a) + A

N = 30
A, B = -5, 5
for i in range(N):
        x = scale(N-1, 0, 0, 7, i)
        y = sin(x)
        w = scale(60, x, 0, 20, y)
        print(int(w)*" ", "*")
#поправить- фото в телефоне
