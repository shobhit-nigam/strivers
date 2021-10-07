lista = ['w', 'o', 'r', 'l', 'd', ' ', 'p', 'e', 'a', 'c', 'e']

def only_vowels(ch):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return ch in vowels


listx = list(filter(only_vowels, lista))
print(listx)
