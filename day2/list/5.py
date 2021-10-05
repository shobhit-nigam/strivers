# functions
lista = ['aa', 'hh', 'aa', 'KK', 'dd', 'rr', 'ff', '25', 'WW']
listnum = [23, 67, 89.34, 12, 94, 67]

print("lista =",lista)
print("----")
lista.reverse()
print("lista =",lista)
print("----")
lista.sort()
print("lista =",lista)
print("----")
lista.sort(reverse=True)
print("lista =",lista)
print("----")

listx = [23, '78', 'aa']
#error
listx.sort()
