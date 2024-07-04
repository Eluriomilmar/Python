#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
num = random.randint(0,5)
aux = int(input("Insira número inteiro entre 0 e 5: "))
print(f"\nO computador jogou: {num}\nVocê tentou adivinhar: {aux}")
if num == aux:
    print(f"Você acertou o número misterioso!")
else:
    print("Você não acertou o número misterioso!")