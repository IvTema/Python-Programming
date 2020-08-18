#https://stepik.org/lesson/3378/step/2?unit=961

import requests
with open('dataset_3378_2.txt', 'r') as inf:
    r = requests.get(inf.readline().strip())
    print(len(r.text.splitlines()))