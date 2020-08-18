# https://stepik.org/lesson/3369/step/8?unit=952

a = int(input())
b = 0
for i in range (a):
    for j in range(i+1):
        b += 1
        if b > a:
            break
        print(i+1, end=' ')