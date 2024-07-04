#Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas, o nome com todas as letras minúsculas, quantas letras ao todo(s/ espaços) e quantas letras tem o primeiro nome
nome = input("Insira o nome completo: ")
print(f"Nome maiúsculo: {nome.upper()}")
print(f"Nome minúsculo: {nome.lower()}")
print(f"Quantidade de letras: {len(nome) - nome.count(" ")}")
print(f"O primeiro nome tem {len(nome.split()[0])} letras")