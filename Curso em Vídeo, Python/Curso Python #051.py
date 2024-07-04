#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
primeiro = int(input("Insira o primeiro termo da progressão aritmética: "))
progressao = int(input("Insira o a razão da progressão aritmética: "))
for i in range(10):
    print(f"O termo {i} é igual a {primeiro + progressao * i}")