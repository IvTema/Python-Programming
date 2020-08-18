# https://stepik.org/lesson/5047/step/7?unit=1086
a = (input())
if (int(a[0])+int(a[1])+int(a[2])) == (int(a[-1])+int(a[-2])+int(a[-3])):
    print("Счастливый")
else:
    print("Обычный")