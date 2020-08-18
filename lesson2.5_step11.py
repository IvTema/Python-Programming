# https://stepik.org/lesson/3368/step/11?unit=951
a = sorted([int(i) for i in input().split()])
b = []
if len(a) != 1:
    for i in range (len(a)-1):
        if a.count(a[i]) > 1 and a[i] != a[i+1]:
            print(a[i], end=(' '))
    if a.count(a[-1]) > 1:
        print(a[-1])