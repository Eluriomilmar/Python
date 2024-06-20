##Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
#Refaça o exercício acima lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
termo = float(input("Insira o primeiro termo da progressão: "))
razao = float(input("Insira a razão da PA: "))
i = 0
while i < 10:
    print(f"O termo {i+1} é igual a {termo + razao * i}")
    i += 1