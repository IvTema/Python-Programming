# https://stepik.org/lesson/3368/step/10?unit=951
a = [int(i) for i in input().split()]
b = len(a)
if b == 1:
    print(a[0])
else:
    c = 0
    d = 0
    a.insert(0, a[-1])
    a.append(a[1])
    for i in range (b):
        i += 2
        d = a[c] + a[i]
        c += 1
        print(d, end=' ')