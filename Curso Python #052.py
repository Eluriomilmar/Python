#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
p = int(input("Insira número a ser aferido se é primo: "))
for i in range(2, p):
    if p%i == 0:
        print(f"O número {p} não é primo.")
        break
    elif i == p-1:
        print(f"O número {p} é primo.")