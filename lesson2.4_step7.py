# https://stepik.org/lesson/3367/step/7?unit=950
a = input()
b = 0
c = 1
d = 1
e = 0
f = 1
g = 1
h = -1
j = -2
k = 1
for i in range (len(a)-1):  # считаем кол-во смен букв в ряде
    if a[b] == a[c]:
        b += 1
        c += 1
    else:
        b += 1
        c += 1
        d += 1
for i in range (d-1):  # запускаем цикл - 1 смена буквы в ряде, иначе ошибка
    while a[e] == a[f]:
        e += 1
        f += 1
        g += 1
    print(a[e] + str(g), end='')
    if a[e] != a[f]:
        e += 1
        f += 1
        g = 1
if d == 1:                     # если все знаки в строке одинаковые
    print(a[0] + str(len(a)))
else:
    while a[h] == a[j]:       # надо посчитать последний символ в ряде
        h -= 1
        j -= 1
        k += 1
    print(a[h] + str(k))