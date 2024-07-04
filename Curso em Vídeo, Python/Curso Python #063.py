#Escreva um programa que leia um número n inteiro qualquer e mostre na tela os primeiros elementos de uma sequência de fibonacci.
n = int(input("Insira quantos elementos de fibonacci se deseja calcular: "))
i = 0
while i < n:
    if i == 0:
        primeiro = 0
        segundo = 0
        print(f"{primeiro}", end = "")
        i = i + 1
    elif i == 1:
        primeiro = 1
        segundo = 0
        print(f", {primeiro}", end = "")
        i = i + 1
    elif i == 2:
        primeiro = primeiro + segundo
        segundo = 1
        print(f", {primeiro}", end ="")
        i = i + 1
    else:
        aux = primeiro
        primeiro = segundo + primeiro
        segundo = aux
        print(f", {primeiro}", end = "")
        i = i + 1
