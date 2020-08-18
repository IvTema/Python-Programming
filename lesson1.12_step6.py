# https://stepik.org/lesson/5047/step/6?unit=1086
a = int(input())
t=("программист")
ta=("программиста")
tov=("программистов")
if 11<=a<=14 or (a-11)%100==0 or (a-12)%100==0 or (a-13)%100==0 or (a-14)%100==0:
    print(a, tov)
elif (a-1)%10==0 or a==1:
    print(a, t)
elif (a-2)%10==0 or a==2:
    print(a, ta)
elif (a-3)%10==0 or a==3:
    print(a, ta)
elif (a-4)%10==0 or a==4:
    print(a, ta)
else:
    print(a, tov)
