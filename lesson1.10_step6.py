# https://stepik.org/lesson/2414/step/6?unit=931
year = int(input())
if year%4==0 and year%100!=0 or year%400==0:
    print("Високосный")
else:
    print("Обычный")