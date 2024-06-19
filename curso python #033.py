#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
num = float(input("Insira o primeiro número: "))
maior = num
menor = num
num = float(input("Insira o segundo número: "))
if num > maior:
    maior = num
elif num < menor:
    menor = num
num = float(input("insira o terceiro número: "))
if num> maior:
    maior = num
elif num < menor:
    menor = num
print(f"O maior número é {maior} e o menor número é {menor}.")