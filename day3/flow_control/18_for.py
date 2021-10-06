avengers = {'thor':'hammer', 'captain':['shield', 'hammer'],
    'iron man':'suit', 'black widow':'elegance'}

list_keys = list(avengers)

for x in list_keys[::2]:
    print(x)
    print(avengers[x])
    print("---")
