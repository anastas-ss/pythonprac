a = input().split()
box = []
box.append(a[4])
box.append(a[1])
box.append(a[0])
print(*box, sep=", ")
