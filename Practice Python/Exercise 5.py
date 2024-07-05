"""write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes."""
import random

def gera_listas():
    a = random.randint(1,10)
    lista = []
    for i in range(a):
        lista.append(random.randint(1,10))
    return lista
def iguais(a, b):
    c = []
    for i in range(len(a)):
        for j in range(len(b)):
            if b[j] == a[i]:
                if b[j] not in c:
                    c.append(b[j])
    return c

a = gera_listas()
b = gera_listas()
print(f"Lista A: {a}\nLista B: {b}")
c = iguais(a, b)
print(c)