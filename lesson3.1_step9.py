# https://stepik.org/lesson/3372/step/9?unit=955

def modify_list(l):
    a = []
    for i in range (len(l)):
        if l[i] % 2 == 0:
            l[i] //= 2
            a.append(l[i])
    del l[:]
    for i in range(len(a)):
        l.append(a[i])

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]