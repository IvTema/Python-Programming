# https://stepik.org/lesson/3373/step/6?unit=956

from collections import Counter
a = [(i) for i in input().lower().split()]
cntr = Counter(a)
for key, value in dict(cntr).items():
    print(key, value)
