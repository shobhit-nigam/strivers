ca = {'green', 'red', 'yellow', 'green', 'black', 'red', 'white'}
print("type of ca =", type(ca))
cb = {'green', 'black', 'red', ('red', 'yellow', 'green')}
print("type of cb =", type(cb))
# error
cb = {'green', 'black', 'red' ['red', 'yellow', 'green']}
