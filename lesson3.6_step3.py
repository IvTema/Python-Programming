# https://stepik.org/lesson/3378/step/3?unit=961

import requests
fn = '699991.txt'
fl = fn.split()
while fl[0] != 'We':
    r =requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + fn)
    fn = r.text
    fl = fn.split()
print(fn)