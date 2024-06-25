"""Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) QUantos números foram digitados.
B) A lista de valores ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista"""
cont = True
total_num = 0
lista = []
while cont == True:
    num = int(input("Insira número a ser adicionado na lista: "))
    lista.append(num)
    total_num += 1
    if str(input("Deseja continuar? S/N: ")).upper() == "S":
        cont = True
    else:
        cont = False
lista.sort(reverse = True)
print(f"Foram digitados {len(lista)} números.\nA lista ordenada de forma decrescente é igual a: {lista}\nE ", end = "")
if 5 in lista:
    print(f"O número 5 existe na lista.")
else:
    print(f"O número 5 não existe na lista.")