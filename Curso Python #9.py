#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
num = float(input("Insira número para que seja efetuado o cálculo da tabuada: "))
for x in range(10):
    print(f"{x}*{num}={x*num}")