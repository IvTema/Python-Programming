# https://stepik.org/lesson/3366/step/3?unit=949
a = int(input())
b = int(input())
c = int(input())
d = int(input())
for j in range (c, d+1):
    print('\t', j, end='\t')
print()
for i in range (a, b+1):
    print(i, end='')
    for f in range(c, d + 1):
        print('\t', i*f, end='\t')
    print()
