# __builtins__

print("hello")

display = print

display("hello")

print = 10

display(print + 34)

print = __builtins__.print

# __builtins__.print
print("hello")
