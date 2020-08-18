# https://stepik.org/lesson/3363/step/2?unit=1135

with open('C:/dataset_3363_2 (1).txt', 'r') as inf:
    s1 = (inf.readline().strip())+' '
b = ''   # для записи числа
c = len(s1)
input_message = ''   # на 'w'
for i in range (c-1):
    if s1[i].isalpha(): # буква
        a = s1[i]
    else:
        if s1[i+1].isdigit(): # если цифра в  i + 1
            b += s1[i] # добавляем нынешнюю
        else:
            b += s1[i]
            input_message += str(a)*int(b) # иначе на вывод цифры*буквы
            b = ''
with open('C:/dataset_3363_2 (1).txt', 'w') as ouf:
    ouf.write(str(input_message))