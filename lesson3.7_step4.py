# https://stepik.org/lesson/3380/step/4?unit=963

sample_quantity = int(input())
NS = 0
WE = 0
sample = []
for i in range(sample_quantity):
    sample = [j for j in input().lower().split()]
    if 'север' in sample:
        NS += int(sample[-1])
    if 'юг' in sample:
        NS -= int(sample[-1])
    if 'восток' in sample:
        WE += int(sample[-1])
    if 'запад' in sample:
        WE -= int(sample[-1])
print(WE, NS, sep=(' '))