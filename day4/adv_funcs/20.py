lista = [(20, 10), (10, 30), (5, 6), (10, 5) ,(6, 8)]
listb = [3, 8, 10, 6, 11, 20]


listx = list(filter(lambda x: x%2==0, listb))
print(listx)
