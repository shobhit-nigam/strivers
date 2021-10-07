fa = open("one.txt", "r")

stra = fa.read()
fa.close()

lista = stra.splitlines()

col = []

for line in lista[1:]:
    temp = line.split(',')
    col.append(temp[2])

print(col)
