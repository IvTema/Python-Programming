# https://stepik.org/lesson/3365/step/4?unit=948
a = 10
while a <= 100:
    a=int(input())
    if a > 100:
        break
    if a < 10:
        continue
    print(a)