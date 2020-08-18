# https://stepik.org/lesson/3369/step/11?unit=952

row_coll = int(input())
first_list = [[0 for j in range (row_coll)] for i in range (row_coll)]
a = 0
b = row_coll
c = -2
d = -2
e = 1
f = 0
h = 0
second_list = [0,0,0,0]
if row_coll in range (2):
    print(row_coll)
for i in range (row_coll*4):
        if i < row_coll:
            first_list[0][i] = i+1
        if i >= row_coll and i < row_coll*2:
            first_list[a][row_coll-1] = b
            a += 1
            b += 1
        if i > row_coll*2 and i < row_coll*3:
            first_list[row_coll - 1][c] = b
            c -= 1
            b += 1
        if i > row_coll*3 and i < row_coll*4-1:
            first_list[d][0] = b
            d -= 1
            b += 1
while second_list.count(0) != 0 and row_coll > 2:
    if first_list[f+1][h] > first_list[f][h+1] and first_list[f+1][h+2] == 0 and first_list[f+2][h+1] == 0:
        first_list[f+1][h+1] = b
        b += 1
        h += 1
    elif first_list[f][h+1] > first_list[f+1][h+2] and first_list[f+1][h] == 0 and first_list[f+2][h+1] == 0:
        first_list[f+1][h+1] = b
        b += 1
        f += 1
    elif first_list[f+1][h+2] > first_list[f+2][h+1] and first_list[f][h+1] == 0 and first_list[f+1][h] == 0:
        first_list[f+1][h+1] = b
        b += 1
        h -= 1
    elif first_list[f+2][h+1] > first_list[f+1][h] and first_list[f][h+1] == 0 and first_list[f+1][h+2] == 0:
        first_list[f+1][h+1] = b
        b += 1
        f -= 1
    else:
        second_list[0] = first_list[f + 1][h]
        second_list[1] = first_list[f][h + 1]
        second_list[2] = first_list[f + 1][h + 2]
        second_list[3] = first_list[f + 2][h + 1]
        if second_list.count(0) == 1:
            first_list[f+1][h+1] = b
            if first_list[f + 1][h] == 0:
                b += 1
                h -= 1
            elif first_list[f][h + 1] == 0:
                b += 1
                f -= 1
            elif first_list[f + 1][h + 2] == 0:
                b += 1
                h += 1
            elif first_list[f + 2][h + 1] == 0:
                b += 1
                f += 1
if row_coll not in range (2):
    if first_list[f+1][h+1] == 0:
        first_list[f+1][h+1] = b
    for i in range(row_coll):
        print(*first_list[i])