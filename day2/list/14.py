# references

lista = ['aa', 'hh', 'aa', 'KK', 'dd', 'rr']
listb = ['ff', '25', 'WW']
listc = [20, 30, listb.copy(), [45, 67]]

xb = listb.copy()
print("listb =", listb)
print("xb =", xb)
print("listc =", listc)

listb.sort()
listb.insert(2, 'cc')
listb.append('rr')
listb.reverse()

print("------")
print("listb =", listb)
print("xb =", xb)
print("listc =", listc)
