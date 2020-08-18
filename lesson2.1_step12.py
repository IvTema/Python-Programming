# https://stepik.org/lesson/3364/step/12?unit=947
a = int(input())
b = int(input())
c = 1
while c % a != 0 or c % b != 0:
    c += 1
print(c)