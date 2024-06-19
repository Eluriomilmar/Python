#Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar
num = int(input("Insira número inteiro: "))
if num%2 == 0:
    print(f"O número {num} é par.")
else:
    print(f"O número {num} é ímpar.")