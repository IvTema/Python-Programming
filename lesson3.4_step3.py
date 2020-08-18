# https://stepik.org/lesson/3363/step/3?unit=1135

all_words = []
with open('C:/dataset_3363_3.txt', 'r') as inf:
    for line in inf:
        all_words += [str(i) for i in line.strip().lower().split()] # заполняю список
all_words_dict = {}
for i in all_words:
    all_words_dict[i] = all_words.count(i) # перегоняю в словарь
for key in all_words_dict.keys():
    if all_words_dict.get(key) == max(all_words_dict.values()): # хитроумно сравниваю текущее значение с максимальным
        print(key, all_words_dict.get(key))
        break