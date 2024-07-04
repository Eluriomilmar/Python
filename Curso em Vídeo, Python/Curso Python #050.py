#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
soma = 0
for i in range(6):
    x = int(input("Insira número a ser somaado. O número somente será somado se for par: "))
    if x%2 == 0:
        soma = soma + x
print(f"A soma total de todos os números pares é igual a {soma}")