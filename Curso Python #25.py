#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
nome = input("Insira o nome da pessoa: ")
if nome.upper().find("SILVA") != -1:
    print(f"{nome} possui Silva no nome.")
else:
    print(f"{nome} não possui Silva no nome.")