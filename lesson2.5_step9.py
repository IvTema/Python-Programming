# https://stepik.org/lesson/3368/step/9?unit=951
a = [int(i) for i in input().split()]
b = 0
c = a[0]
for i in range (len(a)-1):
    b += 1
    c += a[b]
print(c)