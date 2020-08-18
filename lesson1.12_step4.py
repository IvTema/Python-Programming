# https://stepik.org/lesson/5047/step/4?unit=1086
k=input()
if k == ("круг"):
    a = int(input())
    print(float(3.14*(a**2)))
elif k == ("прямоугольник"):
    a = int(input())
    b = int(input())
    print(float(a*b))
elif k == ("треугольник"):
    a=int(input())
    b=int(input())
    c=int(input())
    p=float((a+b+c)/2)
    print(float((p*(p-a)*(p-b)*(p-c))**(1/2)))