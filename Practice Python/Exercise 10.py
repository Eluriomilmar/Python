"""Write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes."""
from random import randint

def tam_lista():
    while True:
        try:
            tam = int(input("Insira o tamanho da lista, 0 para aleatório: "))
            if tam < 0:
                raise ValueError
        except:
            print("Insira número inteiro maior ou igual a 0")
        else:
            return tam


def gera_lista(tam = 0):
    lista = []
    if tam == 0:
        a = randint(1, 30)
        for i in range(a):
            lista.append(randint(1,100))
    else:
        for i in range(tam):
            lista.append(randint(1,100))
    return lista


def concatenacao(list1, list2):
    list3 = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list2[j] == list1[i] and list2[j] not in list3:
                list3.append(list2[j])
    return list3



lista = concatenacao(gera_lista(tam_lista()), gera_lista(tam_lista()))
print(lista)