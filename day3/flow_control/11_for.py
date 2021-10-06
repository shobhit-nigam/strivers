avengers = {'thor':'hammer', 'captain':['shield', 'hammer'],
    'iron man':'suit', 'black widow':'elegance'}

for k, v in avengers.items():
    print("k =", k)
    print("v =", v)
    if type(v) is list:
        for z in v:
            print("\t", z)
    print("----")
