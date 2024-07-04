"""Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta."""
import random
qtd_jogos = int(input("Quantos jogos deseja jogar? "))
jogos = list()
for i in range(qtd_jogos):
    jogos.append([])
    for j in range(6):
        num = random.randint(1,60)
        if num not in jogos[i]:
            jogos[i].append(num)
        else:
            while num in jogos[i]:
                num = random.randint(1,60)
            jogos[i].append(num)
print(f"Os números sorteados foram: {jogos}")