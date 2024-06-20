#Crie um programa que faça o computador jogar pedra-papel-tesoura com você
import random
opcoes = ["pedra", "papel", "tesoura"]
opcoes = random.choice(opcoes)
escolha = str(input("digite pedra, papel ou tesoura para jogar: ")).lower()
if escolha == "pedra":
    if opcoes == "pedra":
        print("Empate")
    elif opcoes == "papel":
        print("Perdeu")
    else:
        print("Venceu")
elif escolha == "papel":
    if opcoes == "papel":
        print("Empate")
    elif opcoes == "tesoura":
        print("Perdeu")
    else:
        print("Venceu")
elif escolha == "tesoura":
    if opcoes == "tesoura":
        print("Empate")
    elif opcoes == "pedra":
        print("Perdeu")
    else:
        print("Venceu")
else:
    print("Input inválido.")