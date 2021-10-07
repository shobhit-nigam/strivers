listx = ["hello", "how u doing", "hey", "hi"]

print(list(enumerate(listx)))


print(list(enumerate(listx, start=13)))

print(list(enumerate(listx, start=-13)))

help(enumerate)
