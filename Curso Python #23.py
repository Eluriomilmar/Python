#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
num = input("Insira número entre 0 e 9999: ")
num = int(num)
if num >= 0 and num <= 9999:
    unidade = num % 10
    num = num - unidade
    dezena = num % 100
    num = num - dezena
    centena = num % 1000
    num = num - centena
    milhar = num
    num = num - milhar
    print(f"Unidade: {unidade}\nDezena: {dezena/10:.0f}\nCentena: {centena/100:.0f}\nMilhar: {milhar/1000:.0f}")
else:
    print("Argumento inválido")