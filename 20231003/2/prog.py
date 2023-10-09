def sub2(a, b):
    if type(a) == type(b):
        if isinstance(a, list) or isinstance(a, tuple):
            box = []
            for elem in a:
                if elem not in b:
                    box.append(elem)
            if isinstance(a, list):
                return box
            else:
                return tuple(box)
        else:
            return a-b
a, b = eval(input())
print(sub2(a, b))
