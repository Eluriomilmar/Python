#Faça um programa que jogue par ou impar com o computador.
#O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random
cont = 0
while True:
    par_ou_impar = str(input("Escolha entre Par ou Impar: "))
    jogador = int(input("Insira o número para jogar par ou ímpar: "))
    jogada =  random.randint(1,10)
    if par_ou_impar == "par":
        if (jogador + jogada) % 2 == 0:
            print("Você venceu! Jogue novamente.")
            cont += 1
        else:
            print(f"Você perdeu! Foram acumuladas {cont} vitórias.")
            break
    else:
        if (jogador + jogada) % 2 == 1:
            print("Você venceu! Jogue novamente.")
            cont += 1
        else:
            print(f"Você Perdeu! Foram acumuladas {cont} vitórias.")
            break




