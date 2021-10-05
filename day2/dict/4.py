avengers = {'thor':'hammer', 'captain':['shield', 'hammer'],
    'iron man':'suit', 'black widow':'elegance'}

xmen = ['wolverine', 'magneto', 'blue']

marvel = {'xmen':xmen, 'ave':avengers}

print("marvel =", marvel)
print("----")
print("marvel['ave'] =", marvel['ave'])
print("----")
print("marvel['ave']['captain'] =", marvel['ave']['captain'])
print("----")
print("marvel['ave']['captain'][1] =", marvel['ave']['captain'][1])
print("----")
print("marvel['ave']['captain'][1][2] =", marvel['ave']['captain'][1][2])
