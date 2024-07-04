#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
from datetime import datetime
ano = datetime.now().year
maiores = 0
menores = 0
for i in range(7):
    var = int(input(f"Insira o ano de nascimento da pessoa {i+1}: "))
    if ano - var < 18:
        menores = menores + 1
    else:
        maiores = maiores + 1
print(f"{maiores} pessoas já atingiram a maioridade e {menores} ainda são menores de idade.")