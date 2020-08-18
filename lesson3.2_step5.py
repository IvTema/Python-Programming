# https://stepik.org/lesson/3373/step/5?unit=956

def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    elif key not in d and 2*key in d:
        d[2*key].append(value)
    elif 2*key not in d:
        d[2*key] = [value]

d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}