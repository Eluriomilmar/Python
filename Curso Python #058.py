#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
#Melhore o jogo acima para que ele seja jogado até o jogador acertar um número entre 0 e 10 e mostrando quantos palpites foram necessários para vencer
import random
numero = random.randint(0, 10)
palpite = int(input("Insira número entre 0 e 10: "))
tentativas = 1
while palpite != numero:
    palpite = int(input("Errou! Tente novamente: "))
    tentativas += 1
print(f"Acertou, o número era {numero}, foram efetuadas {tentativas}.")
