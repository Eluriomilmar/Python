a = input("Insira nome do arquivo: ")
dicio = dict()
lista = list()
tupla = tuple()
with open(a, "r") as arquivo:
    for palavras in arquivo:
        palavras = palavras.splitlines()
        for linha in palavras:
            linha = linha.split(" ")
            if linha[0] == "From":
                if linha[1] in dicio:
                    dicio[linha[1]] += 1
                else:
                    dicio[linha[1]] = 1
for i, j in dicio.items():
    tupla = i, j
    lista.append(tupla)
indice = 0
for i in range(len(lista)):
    for j in range(len(lista)-1):
        if lista[j][1] < lista[j+1][1]:
            aux = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = aux
print(f"{lista[0][0]}: {lista[0][1]}")
