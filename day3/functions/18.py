lista = [100, 200, 300, 400]
listb = [77, 88]

def funca(la):              # la = lista
    la[3] = 99
    print("la =", la)

print("lista =", lista)
funca(lista)
print("lista =", lista)
