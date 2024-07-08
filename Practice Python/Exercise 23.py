"""Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000."""


def converte(lista):
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    return lista


def abre(lista):
    with open(lista, "r") as coisa:
        coisalista = list(coisa.read().split("\n"))
    return coisalista


def compara(lista1, lista2):
    lista3 = []
    for i in lista1:
        for j in lista2:
            if j == i:
                lista3.append(j)
    return lista3



happy = converte(abre("happynumbers.txt"))
prime = converte(abre("primenumbers.txt"))
print(compara(happy, prime))











