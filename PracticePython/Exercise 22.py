"""Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen."""


def cria_lista(arq):
    pre = []
    final = []
    with open(arq, "r") as treino:
        vetor = treino.read().split("\n")
        for i in vetor:
            pre.append(i[3:])
        for i in range(len(pre)):
            pre[i] = pre[i].split("/")
            final.append(pre[i][0])
    return final


def cria_dict(trens):
    dicio = dict()
    for i in trens:
        dicio[i] = 0
    for i in trens:
        dicio[i] += 1
    return dicio


lista = cria_lista("Training_01.txt")
dicionario = cria_dict(lista)
for i, j in dicionario.items():
    if i != "":
        print(f"{i}: {j}")