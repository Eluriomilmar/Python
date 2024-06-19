#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"
nome = input("Insira o nome da cidade: ")
if nome.upper().find("SANTO") == 0:
    print("O nome da cidade começa com Santo.")
else:
    print("O nome da cidade não começa com Santo.")
