lista = [(20, 10), (10, 30), (5, 6), (10, 5) ,(6, 8)]
listb = [3, 8, 10, 6, 11]

# print(lista + listb)

def calc(a, b):
    return 2*a + 3*b - 2

listx = list(map(lambda x, y: x[0] if x[0] > y else y, lista, listb))
print(listx)
