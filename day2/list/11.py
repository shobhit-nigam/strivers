# functions
# append vs extend

# part one
lista = ['aa', 'hh', 'aa', 'KK', 'dd', 'rr']
listb = ['ff', '25', 'WW']

print("lista =", lista)
print("len of lista =", len(lista))
lista.append(listb)
print("-----")
print("lista =", lista)
print("len of lista =", len(lista))

print("##################")
# part two
lista = ['aa', 'hh', 'aa', 'KK', 'dd', 'rr']
listb = ['ff', '25', 'WW']

print("lista =", lista)
print("len of lista =", len(lista))
lista.extend(listb)
print("-----")
print("lista =", lista)
print("len of lista =", len(lista))
