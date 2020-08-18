# https://stepik.org/lesson/3380/step/2?unit=963

sample = dict.fromkeys(i for i in input())
code = [i for i in input()]
k = 0
for j in sample:
    sample[j] = code[k]
    k += 1
for_coding = [i for i in input()]
for_decoding = [i for i in input()]
for l in for_coding:
    print(sample.get(l), end=(''))
print('')
for p in for_decoding:
    for k in sample:
        if sample.get(k) == p:
            print(*k, end=(''))