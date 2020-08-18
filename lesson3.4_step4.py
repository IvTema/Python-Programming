# https://stepik.org/lesson/3363/step/4?thread=solutions&unit=1135

all_words = []
countThing = 0
ma = 0
fi = 0
ru = 0
with open('C:/dataset_3363_4.txt', 'r') as inf:
    for line in inf:
        all_words += [[str(i) for i in line.strip().split(';')]]  # заполняю список
        countThing += 1
for i in range (countThing): # счетчики
    ma += int(all_words[i][1])
    fi += int(all_words[i][2])
    ru += int(all_words[i][3])
ma = ma/countThing
fi = fi/countThing
ru = ru/countThing
with open('C:/pyth_work.txt', 'w') as ouf: # заношу
    for line in range(countThing):
        ouf.write(str((int(all_words[line][1]) + int(all_words[line][2]) + int(all_words[line][3]))/3) + '\n')
    ouf.write(str(ma) + " ")
    ouf.write(str(fi) + " ")
    ouf.write(str(ru) + " ")