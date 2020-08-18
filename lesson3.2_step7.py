# https://stepik.org/lesson/3373/step/7?unit=956

duck = {}
n = int(input())
for i in range(n):
    x = int(input())
    if x in duck:
        print(duck.get(x))
    else:

        duck[x] = f(x)
        print(duck.get(x))