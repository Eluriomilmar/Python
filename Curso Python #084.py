"""Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""
cont = "S"
pessoas = list()
temp = list()
maior = 0
menor = 0
while cont == "S":
    temp.append(str(input("Nome: ")))
    temp.append(float(input("Peso: ")))
    if len(pessoas) == 0:
        maior = temp[1]
        menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    pessoas.append(temp[:])
    temp.clear()
    cont = str(input("Deseja continuar? (S/N): ")).upper()
    if cont == "N":
        break
    elif cont != "S":
        while cont != "S" and cont != "N":
            cont = str(input("Input inválido, tente novamente: ")).upper()
    if cont == "N":
        break
print(f"Foram cadastradas {len(pessoas)} pessoas.\nAs pessoas mais pesadas pesam {maior}, e são elas: ", end="")
for i in range(len(pessoas)):
    if maior == pessoas[i][1]:
        print(f"{pessoas[i][0]} ", end="")
print(f"\nAs pessoas mais leves pesam {menor}, e são elas: ", end = "")
for i in range(len(pessoas)):
    if menor == pessoas[i][1]:
        print(f"{pessoas[i][0]} ", end = "")