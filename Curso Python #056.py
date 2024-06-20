#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: A média de idade do grupo. 
#Qual o nome do homem mais velho e quantas mulheres tem menos de 20 anos
from datetime import datetime
ano = datetime.now().year
media = 0
homem_velho_nome = ""
homem_velho_idade = 0
mulheres_jovens = 0
for i in range(4):
    nome = str(input(f"Insira o nome da {i+1}ª pessoa: "))
    idade = int(input(f"Insira a idade da {i+1}ª pessoa: "))
    sexo = str(input(f"Insira o sexo da {i+1}ª pessoa: ")).upper()
    media = media + idade
    if sexo == "M":
        if idade > homem_velho_idade:
            homem_velho_idade = idade
            homem_velho_nome = nome
    if sexo == "F" and idade <= 20:
        mulheres_jovens = mulheres_jovens + 1
media = media/4
print(f"A média de idade do grupo é igual a: {media:.0f}\nO nome do homem mais velho é: {homem_velho_nome}\nO grupo possui {mulheres_jovens} mulheres")