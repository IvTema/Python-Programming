# https://stepik.org/lesson/3369/step/10?unit=952

first_list = []
b = [str(i) for i in input().split()]
while b != ['end']:
    first_list += [b]
    b = [str(i) for i in input().split()]
column = len(first_list)
row = len(first_list[0])
new_list = [[0 for j in range(row+2)] for i in range(column+2)]
for i in range (column):
    for j in range (row):
        new_list[i+1][j+1] = first_list[i][j]
for i in range (row):
    new_list[0][i+1] = first_list[column - 1][i]
    new_list[column + 1][i+1] = first_list[0][i]
for i in range (column):
    new_list[i + 1][0] = first_list[i][row - 1]
    new_list[i + 1][row + 1] = first_list[i][0]
for i in range (column):
    for j in range (row):
        first_list[i][j] = int(new_list[i][j+1])
        first_list[i][j] += int(new_list[i+1][j])
        first_list[i][j] += int(new_list[i+1][j+2])
        first_list[i][j] += int(new_list[i+2][j+1])
for i in range (column):
    print(*first_list[i])