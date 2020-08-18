# https://stepik.org/lesson/3380/step/3?unit=963

sample_quantity = int(input())
sample = []
for i in range(sample_quantity):
    sample += [j for j in input().lower().split()]
text_quantity = int(input())
text = []
for i in range(text_quantity):
    text += [j for j in input().lower().split()]
text = set(text)
for i in text:
    if i not in sample:
        print(i)