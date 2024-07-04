"""Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""
def maior(vet):
    for i in range(len(vet)):
        if i == 0:
            maior = vet[i]
        else:
            if vet[i] > maior:
                maior = vet[i]
    if len(vet) == 0:
        return 0
    return maior


lista = list()
i = 0
while True:
    lista.append(float(input("Insira número à lista: ")))
    if lista[i] == 0:
        break
    i += 1
print(maior(lista))