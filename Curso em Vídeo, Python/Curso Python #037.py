#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input("digite algum dos seguintes números para converter o número decimal\n1. Binário\n2. Octal\n3. Hexadecimal\n\n"))
numero = int(input("Digite o número o qual se deseja converter: "))
if num == 1:
    numero = bin(numero)
    print(f"Representação em binário é igual a: {numero}")
elif num == 2:
    numero = oct(numero)
    print(f"Representação em octal é igual a: {numero}")
elif num == 3:
    numero = hex(numero)
    print(f"Representação em hexadecimal é igual a: {numero}")
else:
    print("Argumento inválido, número deve ser inteiro igual a 1, 2 ou 3.\nEncerrando programa.")