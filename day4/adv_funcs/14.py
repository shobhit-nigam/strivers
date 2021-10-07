lista = [20, 10, 5, 4, 6, 8]
listb = [3, 8, 10, 6, 11, 12]

# print(lista + listb)

def calc(a, b):
    return 2*a + 3*b - 2

listx = list(map(calc, lista, listb))
print(listx)
