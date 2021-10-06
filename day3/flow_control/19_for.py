avengers = {'thor':'hammer', 'captain':['shield', 'hammer'],
    'iron man':'suit', 'black widow':'elegance'}

flag = 0

for x in avengers:
    if flag%2 == 0:
        print(x)
        print(avengers[x])
        print("---")
    flag = flag+1
