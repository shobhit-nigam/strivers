lista = ['aa', 'hh', 'aa', 'dd', 'rr', 'ff', 'aa', 'ii']

for i in range(len(lista)):
    if lista[i] == 'hh':
        print("xx is at index", i)
        break
else:
    print("did not find")
