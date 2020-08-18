# https://stepik.org/lesson/2414/step/5?unit=931
A = int(input())
B = int(input())
H = int(input())
if A<=H<=B:
    print("Это нормально")
elif H<A:
    print("Недосып")
elif H>B:
    print("Пересып")