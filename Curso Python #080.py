"""Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção, sem usar o sort().
No final, mostre a lista ordenada na tela."""
lista = []
for i in range(5):
    valor = int(input("Insira valor a ser inserido na liste: "))
    if i == 0:
        lista.append(valor)
    else:
        for j in range(len(lista)):
            if lista[j] > valor:
                aux = lista[j]
                lista[j] = valor
                valor = aux
        lista.append(valor)
print(f"A lista é igual a: {lista}")