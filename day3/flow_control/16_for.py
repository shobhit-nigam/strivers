lista = ['aa', 'hh', 'aa', 'dd', 'rr', 'ff', 'aa', 'ii']

listx = []

for i in range(len(lista)):
    if lista[i] == 'aa':
        listx.append(i)
        if len(listx) == 2:
            break

print(listx)
