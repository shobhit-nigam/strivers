avengers = {'thor':'hammer', 'captain':['shield', 'hammer'],
    'iron man':'suit', 'black widow':'elegance'}

for x in avengers:
    print("x =", x)

print("----")

for x in avengers:
    print("x =", x)
    print("val =", avengers[x])

print("----")

for x in avengers.values():
    print("x =", x)
