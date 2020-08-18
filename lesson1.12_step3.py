# https://stepik.org/lesson/5047/step/3?unit=1086
first=float(input())
second=float(input())
operation=input()
if operation == ("mod") and second == 0:
    print("Деление на 0!")
elif operation == ("div") and second == 0:
    print("Деление на 0!")
elif operation == ("/") and second == 0:
    print("Деление на 0!")
elif operation == ("+"):
    print(float(first+second))
elif operation == ("-"):
    print(float(first-second))
elif operation == ("/"):
    print (float(first / second))
elif operation == ("*"):
    print (float(first * second))
elif operation == ("mod"):
    print (float(first % second))
elif operation == ("pow"):
    print (float(first ** second))
elif operation == ("div"):
    print (float(first//second))