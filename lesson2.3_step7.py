# https://stepik.org/lesson/3366/step/7?unit=949
a = int(input())
b = int(input())
z=0
c=0
for j in range (a, b+1):
    if j % 3 == 0:
        z += j
        c += 1
print(z/c)
