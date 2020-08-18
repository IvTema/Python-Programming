# https://stepik.org/lesson/5047/step/5?unit=1086
a = int(input())
b = int(input())
c = int(input())
mi=min(a,b,c)
ma=max(a,b,c)
print(ma)
print(mi)
if mi<a<ma:
    print(a)
elif mi<b<ma:
    print(b)
elif mi<c<ma:
    print(c)
elif a==ma and b==ma and c==ma:
    print(ma)
elif a==ma and b==ma or b==ma and c==ma or a==ma and c==ma:
    print(ma)
elif a==mi and b==mi or b==mi and c==mi or a==mi and c==mi:
    print(mi)
