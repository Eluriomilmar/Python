#Faça um programa que leia um número qualquer e mostre seu fatorial
num = int(input("Insira número para o qual será relizado o cálculo do fatorial: "))
print(f"O resultado do fatorial de {num} é: ", end = "")
res = 1
while num > 1:
    res = res * num
    num = num - 1
print(f"{res}")