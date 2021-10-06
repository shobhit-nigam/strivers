def boil(data):
    print('boiled', data)

def gravy(data):
    print(data, 'gravy')

def fry(data):
    print("fried", data)

###############
# high order functions

def eat(gen, datb):
    gen(datb)

eat(fry, "potato")
# fry("potato")
