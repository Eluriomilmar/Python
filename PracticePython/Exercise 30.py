from random import choice


def cria_lista(arq):
    with open(arq, "r") as dicionario:
        vetor = dicionario.read().split("\n")
        return choice(vetor)



print(cria_lista("sowpods.txt"))