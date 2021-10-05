# slicing
ta = ('aa', 'hh', 'aa', 'dd', 'rr', 'ff')

print("type of ta =", type(ta))
print("ta =",ta)

temp = list(ta)
temp.sort()
ta = tuple(temp)

print("----")
print("type of ta =", type(ta))
print("ta =",ta)


# ta = tuple(sorted(ta))
