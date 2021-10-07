fa = open("names.txt", "r")

stra = fa.read(5)
print(stra)

stra = fa.read(5)
print(stra)

print(fa.tell())

fa.seek(2)
stra = fa.read(5)
print(stra)
fa.close()
