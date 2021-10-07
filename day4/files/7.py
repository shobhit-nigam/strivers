
with open("names.txt", "r") as fa:
    lista = fa.readlines()

fb = open("new_names.txt", "w")

for line in lista:
    if line[-6:] == 'stark\n':
        fb.write(line)

fb.close()
