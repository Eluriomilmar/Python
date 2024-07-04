"""Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente."""
num = [[], []]
while True:
    numero = int(input("Insira número inteiro: "))
    if numero%2 == 0:
        num[0].append(numero)
    else:
        num[1].append(numero)
    if len(num[0]) + len(num[1]) == 7:
        break
num[1].sort()
num[0].sort()
print(f"O números pares, em ordem crescente, são: {num[0]}\nOs números ímpares, em ordem crescente, são: {num[1]}")