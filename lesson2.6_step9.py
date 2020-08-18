# https://stepik.org/lesson/3369/step/9?unit=952

a = [int(i) for i in input().split()]
b = int(input())
c = a.count(b)
if c != 0:
    for i in range (c):
        d = a.index(b)
        print(d, end=(' '))
        a[d] = sum(a)
else:
    print("Отсутствует")